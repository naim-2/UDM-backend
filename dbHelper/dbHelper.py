# create tables
CREATE_USER = (
    "CREATE TABLE IF NOT EXISTS users (username TEXT, firstname TEXT, lastname TEXT, phonenumber TEXT, email TEXT, password TEXT, status TEXT, PRIMARY KEY (username, email));"
)
CREATE_SELLER = (
    "CREATE TABLE IF NOT EXISTS seller (username TEXT, productname TEXT, category TEXT, photo TEXT, productdetails TEXT, price INTEGER, quantity INTEGER, reviews TEXT, PRIMARY KEY (username, productname));"
)

# insert into tables
INSERT_USER = "INSERT INTO users (username, firstname, lastname, phonenumber, email, password, status) VALUES (%s, %s, %s, %s, %s, %s, %s);"
INSERT_SELLER = "INSERT INTO seller (username, productname, category, photo, productdetails, price, quantity, reviews) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

# view from tables
GET_USER = "SELECT * FROM users WHERE username=(%s);"
GET_USER_LOGIN = "SELECT * FROM users WHERE username=(%s) AND password=(%s)"
GET_EMAIL = "SELECT * FROM users WHERE email=(%s);"
GET_SELLER = "SELECT * FROM seller WHERE username=(%s) AND productname=(%s);"
GET_PRODUCT_CATEGORY = "SELECT * FROM seller WHERE category=(%s);"
GET_PRODUCTNAME = "SELECT * FROM seller WHERE productname=(%s) AND category=(%s);"
GET_PRODUCT_FILTER = "SELECT * FROM seller WHERE productname=(%s) AND category=(%s) AND price>=(%s) AND price<=(%s);"
GET_PRODUCT_SELLER = "SELECT * FROM seller WHERE username=(%s);"
GET_REVIEWS = "SELECT reviews FROM seller WHERE username=(%s) AND productname=(%s)"
GET_SELLER_DETAILS = "SELECT * FROM user WHERE username=(%s);"

# update tables
UPDATE_USER = "UPDATE users SET firstname=(%s), lastname=(%s), phonenumber=(%s), email=(%s), password=(%s) WHERE username=(%s);"
UPDATE_USER_STATUS = "UPDATE users SET status=(%s) WHERE username=(%s);"
UPDATE_PRODUCT = "UPDATE seller SET photo=(%s), productdetails=(%s), price=(%s), quantity=(%s) WHERE username=(%s) AND productname=(%s);"
INSERT_REVIEW = "UPDATE seller SET reviews=(%s) WHERE username=(%s) and productname=(%s);"

# delete from tables
DELETE_USER = "DELETE FROM users WHERE username=(%s);"
DELETE_PRODUCT = "DELETE FROM seller WHERE username=(%s) AND productname=(%s);"
