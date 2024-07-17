#!/usr/bin/env python3.9


from models.admin import Admin
from models.user import User
from models.challenge import Challenge

# Example usage
admin = Admin(username="admin1", password="password123")
user = User(name="user1", password="userpass")
challenge = Challenge(
    name="Challenge1",
    description="Solve this challenge",
    input="input",
    output="output",
    difficulty="easy",
    starter_function="def solve(): pass",
    examples="['example1', 'example2']"
)

print(admin)
print(user)
print(challenge)

admin.add_challenge(challenge)
user.submit_challenge(challenge)
