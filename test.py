import database

database.create_user("sarah","12345")

print(database.check_password("sarah","1234"))
#print(database.check_user("sarah"))
#database.save_login("ab","ba","ca","code")

#database.create_user("Aisha","12345")
#database.delete_user("sarah")