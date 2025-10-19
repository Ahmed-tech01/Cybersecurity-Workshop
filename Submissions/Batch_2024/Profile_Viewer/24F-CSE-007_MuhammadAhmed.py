# 24F-CSE-007_MuhammadAhmed

# Data
users = {
    "023": {"name": "Aliyan 23", "age": 21, "department": "CSE", "email": "aliyan@example.com"},
    "007": {"name": "Muhammad Ahmed ", "age": 21, "department": "CSE", "email": "ahmed@example.com"},
    "002": {"name": "shayan 23", "age": 20, "department": "CSE", "email": "shayan@example.com"},
    "016": {"name": "Sanaullah choohan", "age": 19, "department": "CSE", "email": "sanaullah@example.com"},
}

# input id
user_id = input("Enter User ID: ")

# show profile
if user_id in users:
    print("\n--- User Profile ---")
    for key, value in users[user_id].items():
        print(f"{key.capitalize()}: {value}")
else:
    print("Invalid User ID! Please try again.")
