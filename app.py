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
            cursor.execute(GET_USERS, (username, ))
            if(cursor.fetchall()==[]):
                cursor.execute(INSERT_USER, (
                    username, firstname, lastname, phonenumber, email, password, status
                ))
                return jsonify({'message': 'Signed Up successfully!'})
    return jsonify({'message': 'Username already exists!'})

# update user details
@app.route('/updateUser', methods=['PUT'])
def add_user():
    username = request.get_json()['username']
    firstname = request.get_json()['firstname'] 
    lastname = request.get_json()['lastname']
    phonenumber = request.get_json()['phonenumber']
    email = request.get_json()['email']
    password = request.get_json()['password']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USER)
            if(cursor.fetchall()==[]):
                cursor.execute(UPDATE_USER, (
                    firstname, lastname, phonenumber, email, password, username
                ))
                return jsonify({'message': 'Details updated successfully!'})
    return jsonify({'message': 'Details have not been updated!!'})

if __name__ == '__main__':
    app.run()