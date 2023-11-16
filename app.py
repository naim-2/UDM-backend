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
                cursor.execute(GET_EMAIL, (email, ))
                if(cursor.fetchall()==[]):
                    cursor.execute(INSERT_USER, (
                        username, firstname, lastname, phonenumber, email, password, status
                    ))
                    return jsonify({'message': 'Signed Up successfully!'})
                return jsonify({'message': 'Email already exists!'})    
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
@app.route('/deleteUser/<usernmae>', methods=['DELETE'])
def delete_user(username):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USER)
            cursor.execute(DELETE_USER, (username, ))
            return jsonify({'message': 'User deleted successfully!'})
        
# user log in
@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USER)
            cursor.execute(GET_USER_LOGIN, (username, password))
            if(cursor.fetchall()==[]):
                return jsonify({'message': 'Wrong email or password!'})
            return jsonify({'message': 'Logged in successfully!'})
                

# add product
@app.route('/addProduct', methods=['POST'])
def add_product():
    username = request.get_json()['username']
    productname = request.get_json()['productname']
    category = request.get_json()['category']
    photo = request.get_json()['photo']
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
                    username, productname, category, photo, productdetails, price, quantity, reviews
                ))
                return jsonify({'message': 'Product details added successfully!'})
            else:
                return jsonify({'message': 'Product name already exists!'})

# update product
@app.route('/updateProduct', methods=['PUT'])
def update_product():
    username = request.get_json()['username']
    productname = request.get_json()['productname']
    photo = request.get_json()['photo']
    productdetails = request.get_json()['productdetails']
    price = request.get_json()['price']
    quantity = request.get_json()['quantity']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_SELLER)
            cursor.execute(UPDATE_PRODUCT, (
                photo, productdetails, price, quantity, username, productname
            ))
            return jsonify({'message': 'Product details updated successfully!'})

# view product
@app.route('/viewProduct', methods=['GET'])
def view_product():
    category = request.args.get('category')
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_SELLER)
            cursor.execute(GET_PRODUCT_CATEGORY, (category, ))
            products = cursor.fetchall()
            if(products==[]):
                return jsonify({'message': 'There are no products in this category!'})
            return jsonify(products)
        
# search for a product
@app.route('/searchProduct', methods=['GET'])
def search_product():
    productname = request.args.get('productname')
    category = request.args.get('category')
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_SELLER)
            cursor.execute(GET_PRODUCTNAME, (productname, category))
            product = cursor.fetchall()
            if(product==[]):
                return jsonify({'message': 'There is no product with such a name!'})
            return jsonify(product)

# filter product
@app.route('/filterProduct', methods=['GET'])
def filter_product():
    productname = request.args.get('productname')
    category = request.args.get('category')
    minprice = request.args.get('minprice')
    maxprice = request.args.get('maxprice')
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_SELLER)
            cursor.execute(GET_PRODUCT_FILTER, (productname, category, minprice, maxprice))
            allproducts = cursor.fetchall()
            if(allproducts==[]):
                return jsonify({'message': 'There is no product with such a price range!'})
            return jsonify(allproducts)

# view products for seller
@app.route('/viewSellerProduct', methods=['GET'])
def view_seller_product():
    username = request.args.get('username')
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_SELLER)
            cursor.execute(GET_PRODUCT_SELLER, (username, ))
            allproducts = cursor.fetchall()
            if(allproducts==[]):
                return jsonify({'message': 'You have no products yet!'})
            return jsonify(allproducts)
        
# delete product
@app.route('/deleteProduct/<username>/<productname>', methods=['DELETE'])
def delete_product(username, productname):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_SELLER)
            cursor.execute(DELETE_PRODUCT, (username, productname))
            return jsonify({'message': 'Product has been deleted successfully!'})

# post review
@app.route('/postReview', methods=['PUT'])
def post_review():
    username = request.get_json()['username']
    productname = request.get_json()['productname']
    reviews = request.get_json()['reviews']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_SELLER)
            cursor.execute(GET_REVIEWS, (username, productname))
            if(cursor.fetchall()==[]):
                cursor.execute(INSERT_REVIEW, (
                    reviews, username, productname
                ))
                return jsonify({'message': 'Review added successfully!'})
            else:
                newreviews = cursor.fetchall() + "!@#$%^&*()" + username + "!@#$%^&*()" + reviews
                cursor.execute(INSERT_REVIEW, (
                    newreviews, username, productname
                ))
                return jsonify({'message': 'Review added successfully!'})
            
# # update review
# @app.route('/updateReview', methods=['PUT'])
# def update_review():
#     username = request.get_json()['username']
#     productname = request.get_json()['productname']
#     reviews = request.get_json()['reviews']
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(CREATE_SELLER)
#             cursor.execute(GET_REVIEWS, (username, productname))
#             databasereviews = cursor.fetchall()
#             newreviews = ""
#             for i in databasereviews.split("!@#$%^&*()"):
#                 if i==reviews:
                    
#                 newreviews += i + "!@#$%^&*()"

#             newreviews = cursor.fetchall() + "!@#$%^&*()" + reviews
#             cursor.execute(INSERT_REVIEW, (
#                 newreviews, username, productname
#             ))
#             return jsonify({'message': 'Review added successfully!'})

# view sellers' details
@app.route('/viewSeller', methods=['GET'])
def view_seller():
    username = request.args.get('username')
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_SELLER)
            cursor.execute(GET_SELLER_DETAILS, (username, ))
            details = cursor.fetchall()
            firstname = details[0][1]
            lastname = details[0][2]
            phonenumber = details[0][3]
            email = details[0][4]
            sellerDetails = [firstname, lastname, phonenumber, email]
            return jsonify(sellerDetails)
        
if __name__ == '__main__':
    app.run()
