#FUNCTIONS:
#       check_user(user)
#       create_user(user,pwd)
#       check_password(username,password)
#       save_login(user,pwd,url,name):
#       modify_login_pass(name)
#       update_login_pass(name,pwd)
#       print_login(user)

import mysql.connector

#Establishing the connection between python and MYSQL workbench
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MySQL@root26",
    database = "loginBot"
)
# Checks user in the database - TESTED
def check_user(user):
    cursor = mydb.cursor(buffered=True)
    sql = "SELECT* from user_info where u_name = %s"

    cursor.execute(sql,(user,))
    db_info = cursor.fetchone()

    if db_info is None:
        print("User not found")
        return False
    else:
        #print("User exists ",user)
        return True
#adding user into the database
##################
# TO BE FIXED 
##################
# it does not checks wheter the the user is already there or not
def create_user(user,pwd):
    cursor = mydb.cursor()
    sql = "INSERT INTO user_info(u_name,u_pwd) VALUES (%s, %s)"
    val = (user,pwd)    

    cursor.execute(sql,val)
    
    if (check_user(user)==True):
        print("User already exists")
    else:
        mydb.commit()
        print("User sucessfully created!")


# Checks password in the database Tested
def check_password(username,password):
    cursor = mydb.cursor()
    sql = "SELECT* from user_info where u_name= %s"

    cursor.execute(sql,(username,))   
    dbinfo = cursor.fetchone()

    db_pwd = dbinfo[2]
    if db_pwd == password:       
        return True
    else:       
        return False

def save_login(user,pwd,url,name):
    cursor = mydb.cursor()
    sql = "INSERT INTO saved_login (u_login,u_pass,u_url,sl_name) values (%s, %s, %s, %s)"
    val = (user,pwd,url,name)

    cursor.execute(sql,(val,))
    mydb.commit()

    print("%s data added successfully!",name)

def delete_user(user):
    cursor = mydb.cursor()
    sql = "DELETE FROM user_info where u_name = %s"
    cursor.execute(sql,(user,))
    mydb.commit()
    print("Data Removed successfully!")

def delete_url_login(name):
    cursor = mydb.cursor()
    sql = "DELETE FROM saved_login where sl_name = %s " 

    cursor.execute(sql,name)
    mydb.commit()


def update_login_pass(name,pwd):
    cursor = mydb.cursor()
    sql = "UPDATE saved_logib SET u_pass = %s where sl_name = %s"
    val = (pwd,name)
    cursor.execute(sql,val)
    mydb.commit()
    print("data updated sucessfully!")

def print_login(user):
    cursor = mydb.cursor()
    sql = "SELECT * from saved_login where uid = %s"
    val = user
    cursor.execute(sql,val)
    results = cursor.fetchall()

    if results:
        for login in results:
            print(login)
    else:
        print("No saved logins found.")