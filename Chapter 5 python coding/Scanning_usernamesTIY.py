current_users = ["jelly" , "colin" , "tyler", "rex", "lewis"]
new_users = ["peter" , "lois" , "stewie" , "JELLY" , "colin"]
for user in new_users:
    if user.lower() in current_users:
        print("This username is already taken")
    else:
        print("This username is available!")