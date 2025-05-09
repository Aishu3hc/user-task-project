
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]


def add_user(users, user):
    users.append(user)


def get_user(users, user_id):
    return next((user for user in users if user["id"] == user_id), None)


def update_user(users, user_id, name=None, email=None):
    user = get_user(users, user_id)
    if user:
        if name:
            user["name"] = name
        if email:
            user["email"] = email
        return True
    return False


def delete_user(users, user_id):
    user = get_user(users, user_id)
    if user:
        users.remove(user)
        return True
    return False


add_user(users, {"id": 3, "name": "Charlie", "email": "charlie@example.com"})
print("After adding Charlie:", users)

update_user(users, 2, name="Bobby")
print("After updating Bob's name:", users)

delete_user(users, 1)
print("After deleting Alice:", users)

print("Retrieving user with ID 3:", get_user(users, 3))
