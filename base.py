import json

def msg_menu():
    print("Please select an action:")
    print("Press 1 - to login")
    print("Press 2 - to register")
    print("Press 3 - to exit")

def register(new_user, new_pass):
    userbase = json.load(open("userbase.json", "r"))
    userbase[new_user] = new_pass
    new_userbase = json.dumps(userbase)
    with open("userbase.json", "w") as f:
        f.write(new_userbase)
        f.close()

def validation(session_username, session_password):
    if session_username in userbase and session_password == userbase[session_username]:
        return True
    else:
        print("Wrong username or password!\n")


msg_menu()

while True:
    action = input("... ")
    if action == "1":
        userbase = json.load(open("userbase.json", "r"))
        session_username = input("Please enter your username: ")
        session_password = input("Please enter you password: ")
        if validation(session_username, session_password):
            break
    elif action == "2":
        new_username = input("Please enter a new username:")
        new_password = input("Please enter a new password:")
        register(new_username, new_password)   
    elif action == "3":
        exit()
    
    msg_menu()
    
    
print(f'\nHi {session_username}!')


