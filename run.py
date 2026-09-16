import bot
import database as db
import icons as i
import files
import time
from colorama import Fore, Back, Style

i.intro()
print("Welcome to Auto-login bot")

files.read_files("options\\Menu1.txt")
option = int(input("Enter your choice : "))

match option:
    case 1:
        print("You have chosen option 1- Login\n Welcome ")
        username = input("Enter your Username : ")
        db.check_user(username)
        attempt = 1
        while(db.check_user(username) == False):
            if attempt>3:
                print("You obviously dont remember you username !\n")
                break
            #while (attempt != 4):
            print(Fore.RED+"Incorrect Username please Try Again"+Style.RESET_ALL)
            time.sleep(0.2)
            username = input("Enter Your Username : ")
            attempt = attempt+1 
        if(db.check_user(username)== True):
            password = input("Enter Password: ")
            Pass_attempts = 1
            while(db.check_password(username,password)== False):
               if Pass_attempts>3:
                print("Are you Trying to Bruteforce!\n")
                break
            #while (attempt != 4):
            print(Fore.RED+"Incorrect Username please Try Again"+Style.RESET_ALL)
            time.sleep(0.2)
            Password = input("Enter Your Password: ")
            Pass_attempts = Pass_attempts+1          
            

        
            
    case 2:
        user = input("Enter the Username: ")
        pwd = input("Enter the password:")
        url = input("Enter the URL to the login page :")
        bot.startBot(user,pwd,url)
    case 3:
        u = input ("Enter username: ")
        p = input("Enter password: ")
        db.create_user(u,p)

save = input("would you like to save login Information y/n: ")
if save == "y":
    if option == 2:
        print("You will have to login first")
    else:
        name = input("name this login information:")
        db.save_login(user,pwd,url,name)
        see = input("would you like to see your saved logins y/n")
        if see == "y":
            db.print_login(us)
        else:
            print("Thank you")


