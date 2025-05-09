import hashlib


users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(username, password):
    if username in users:
        return "Error: User already exists"
    users[username] = hash_password(password)
    return "Created new user"

def login(username, password):
    hashed = hash_password(password)
    if users.get(username) == hashed:
        return "Login Successful"
    return "Login Failed"


print(login("john", "wrongpassword"))   
print(register("john", "mypassword"))   
print(login("john", "mypassword"))      
