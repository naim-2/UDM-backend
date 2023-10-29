import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from dbHelper.dbHelper import *

load_dotenv()

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# SIGNUP
# create user
@app.route('/addUser', methods=['POST'])
def add_user():
    username = request.get_json()['username']
    firstname = request.get_json()['firstname'] 
    lastname = request.get_json()['lastname']
    phonenumber = request.get_json()['phonenumber']
    email = request.get_json()['email']
    password = request.get_json()['password']
    status = request.get_json()['status']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USER)
            cursor.execute(GET_USER, (username, ))
            if(cursor.fetchall()==[]):
                cursor.execute(INSERT_USER, (
                    username, firstname, lastname, phonenumber, email, password, status
                ))
                return jsonify({'message': 'Signed Up successfully!'})
    return jsonify({'message': 'Username already exists!'})

# update user details
@app.route('/updateUser', methods=['PUT'])
def update_user():
    username = request.get_json()['username']
    firstname = request.get_json()['firstname'] 
    lastname = request.get_json()['lastname']
    phonenumber = request.get_json()['phonenumber']
    email = request.get_json()['email']
    password = request.get_json()['password']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USER)
            cursor.execute(UPDATE_USER, (
                firstname, lastname, phonenumber, email, password, username
            ))
            return jsonify({'message': 'Details updated successfully!'})

# change user status
@app.route('/changeUser', methods=['PUT'])
def change_user():
    username = request.get_json()['username']
    status = request.get_json()['status'] 
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USER)
            cursor.execute(UPDATE_USER_STATUS, (
                status, username
            ))
            return jsonify({'message': 'Status changed successfully!'})

# delete user
@app.route('/deleteUser', methods=['DELETE'])
def delete_user():
    username = request.get_json()['username']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USER)
            cursor.execute(DELETE_USER, (username, ))
            return jsonify({'message': 'User deleted successfully!'})
        
# user log in
@app.route('/login', methods=['GET'])
def login():
    username = request.get_json()['username']
    password = request.get_json()['password']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USER)
            cursor.execute(GET_USER, (username, ))
            if(cursor.fetchall()==[]):
                return jsonify({'message': 'No such user exists!'})
            else:
                databasePassword = cursor.fetchall()[5]
                if(password==databasePassword):
                    return jsonify({'message': 'Logged in successfully!'})
                else:
                    return jsonify({'message': 'Wrong password entered!'})

# add product
@app.route('/addProduct', methods=['POST'])
def add_product():
    username = request.get_json()['username']
    productname = request.get_json()['productname']
    category = request.get_json()['category']
    productdetails = request.get_json()['productdetails']
    price = request.get_json()['price']
    quantity = request.get_json()['quantity']
    reviews = []
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_SELLER)
            cursor.execute(GET_SELLER, (username, productname))
            if(cursor.fetchall()==[]):
                cursor.execute(INSERT_SELLER, (
                    username, productname, category, productdetails, price, quantity, reviews
                ))
                return jsonify({'message': 'Product details added successfully!'})
            else:
                return jsonify({'message': 'Product name already exists!'})

# update product
@app.route('/updateProduct', methods=['PUT'])
def update_product():
    username = request.get_json()['username']
    productname = request.get_json()['productname']
    productdetails = request.get_json()['productdetails']
    price = request.get_json()['price']
    quantity = request.get_json()['quantity']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_SELLER)
            cursor.execute(UPDATE_PRODUCT, (
                productdetails, price, quantity, username, productname
            ))
            return jsonify({'message': 'Product details updated successfully!'})

# view product
@app.route('/viewProduct', methods=['GET'])
def view_product():
    category = request.get_json()['category']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_SELLER)
            cursor.execute(GET_PRODUCT_CATEGORY, (category, ))
            if(cursor.fetchall()==[]):
                return jsonify({'message': 'There are no products in this category!'})
            return jsonify(cursor.fetchall())
        
if __name__ == '__main__':
    app.run()