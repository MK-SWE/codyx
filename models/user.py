from base import BaseModel

class User(BaseModel):
    def __init__(self, name, password):
        self.name = name
        self._password = password  # Use private attribute for password
        self.solved_challenges = 0
        self.challenges_history = ""
        self.badges = ""
        self.points_collected = 0
        self.starred_challenges = ""

    @property
    def password(self):
        return self._password  # Read-only password access

    def edit_profile(self, new_name):
        self.name = new_name

    def edit_password(self, current_password, new_password):
        if self._password == current_password:
            self._password = new_password
            return True
        else:
            return False

    def delete_account(self):
        # remove account from database
        pass

    def submit_challenge(self, challenge_id):
        # Update challenge solved data (database update, etc.)
        self.solved_challenges += 1
        self.challenges_history += f"Challenge {challenge_id} completed\n"
        self.points_collected += 10

    def star_challenge(self, challenge_id):
        # Update starred challenges data (database update, etc.)
        self.starred_challenges += f"{challenge_id},"
    
    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username

    def save(self):
        # Implement the save method to save the user to a database
        pass
