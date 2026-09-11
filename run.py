import bot
import database as db

option = int(input("Welcome to the the login bot press the following number:-\n[1]login\n[2]guest user\n[3]Create User\n"))

match option:
    case 1:
        us = input("Enter you username")
        db.check_user(us)
    case 2:
        user = input("Enter the Username: ")
        pwd = input("Enter the password:")
        url = input("Enter the URL to the login page :")
        bot.startBot(user,pwd,url)
    case 3:
        u = input ("Enter username: ")
        p = input("Enter password: ")
        db.create_user(u,p)

