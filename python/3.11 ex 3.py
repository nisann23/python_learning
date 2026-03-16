#a simple user...

#module: auth.py
users = {}

def register(username, password):
    """Registers a new user."""
    if username in users:
        print("Username already exists!")
    else:
        users[username]= password
        print("User registered succesfully!")

def login(username, password):
    """"Authenticates a user"""
    if username in users and users[username] == password:
        print("Login succesful!")
    else:
        print("Invalid username or password.")
