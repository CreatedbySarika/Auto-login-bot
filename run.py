import bot
import database as db
import icons as i
import files

i.intro()
print("Welcome to Auto-login bot")

option = input(files.read_files("options\\Menu1.txt"))

match option:
    case 1:
        username = input("Enter Username: ")
        attempt = 1
        while(db.check_user(username) == False) and attempt<4:
            username = input("Enter Username: ")
            attempt = attempt+1

        else:
            password = input("Enter Password: ")
            
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


