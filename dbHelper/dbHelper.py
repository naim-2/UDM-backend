# create tables
CREATE_USER = (
    "CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, firstname TEXT, lastname TEXT, phonenumber TEXT, email TEXT, password TEXT, status TEXT);"
)
CREATE_SELLER = (
    "CREATE TABLE IF NOT EXISTS seller (username TEXT, productname TEXT, category TEXT, productdetails TEXT, price INTEGER, quantity INTEGER, reviews TEXT, PRIMARY KEY (username, productname));"
)

# insert into tables
INSERT_USER = "INSERT INTO users (username, firstname, lastname, phonenumber, email, password, status) VALUES (%s, %s, %s, %s, %s, %s, %s);"
INSERT_SELLER = "INSERT INTO seller (username, productname, category, productdetails, price, quantity, reviews) VALUES (%s, %s, %s, %s, %s, %s);"

# view from tables
GET_USER = "SELECT * FROM users where username=(%s);"
GET_SELLER = "SELECT * FROM seller where username=(%s) AND productname=(%s);"
GET_PRODUCT_CATEGORY = "SELECT * FROM users where category=(%s)"

# update tables
UPDATE_USER = "UPDATE users SET firstname=(%s), lastname=(%s), phonenumber=(%s), email=(%s), password=(%s) WHERE username=(%s);"
UPDATE_USER_STATUS = "UPDATE users SET status=(%s) WHERE username=(%s);"
UPDATE_PRODUCT = "UPDATE seller SET productdetails=(%s), price=(%s), quantity=(%s) WHERE username=(%s) AND productname=(%s);"

# delete from tables
DELETE_USER = "DELETE FROM users WHERE username=(%s);"