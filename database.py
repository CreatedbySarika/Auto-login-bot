import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MySQL@root26",
    database = "loginBot"
)

def create_user(user,pwd):
    cursor = mydb.cursor()
    sql = "INSERT INTO user_info(u_name,u_pwd) VALUES (%s, %s)"
    val = (user,pwd)

    cursor.execute(sql,val)
    mydb.commit()
    print("User sucessfully created!")

def check_user(user):
    cursor = mydb.cursor()
    sql = "SELECT* from user_info where u_name = %s"

    cursor.execute(sql,user)
    useri = cursor.fetchone()

    if useri:
        print("User exists ",user)
    else:
        print("User not found")

def save_login(user,pwd,url,name):
    cursor = mydb.cursor()
    sql = "INSERT INTO saved_login values (u_login,u_pass,u_url,sl_name) values (user,pwd,url,name)"

    cursor.execute(sql)

    print("%s data added successfully!",name)
    

