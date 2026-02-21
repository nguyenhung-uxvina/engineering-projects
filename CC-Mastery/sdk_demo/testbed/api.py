import json

def get_users(db):
    return db.query("SELECT * FROM users")

def create_user(db, data):
    name = data.get("name")
    email = data.get("email")
    age = data.get("age", 0)
    return db.insert("users", {"name": name, "email": email, "age": age})

def delete_user(db, user_id):
    return db.delete("users", user_id)
