# create tables
CREATE_USER = (
    "CREATE TABLE IF NOT EXISTS user (username TEXT PRIMARY KEY, firstname TEXT, lastname TEXT, phonenumber TEXT, email TEXT, password TEXT, status BIT);"
)
CREATE_SELLER = (
    "CREATE TABLE IF NOT EXISTS seller (username TEXT, productname TEXT, productdetails TEXT, price INTEGER, quantity INTEGER, reviews TEXT, PRIMARY KEY (username, productname));"
)

# insert into tables
INSERT_USER = "INSERT INTO user (username, firstname, lastname, phonenumber, email, password, status) VALUES (%s, %s, %s, %s, %s, %s, %s);"
INSERT_SELLER = "INSERT INTO seller (username, productname, productdetails, price, quantity, reviews) VALUES (%s, %s, %s, %s, %s, %s);"

# get from tables
GET_USERS = "SELECT * FROM user where username = (%s);"