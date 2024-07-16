from models import user
from badges import award_badge, BADGES
from flask import Flask, render_template, flash
from badges.database import db

app = Flask(__name__)

@app.route('/')
def run():
    """Run the app."""
    return render_template('index.html')

    

if __name__ == '__main__':
    app.run()


# route to handle user actions to check and award badges upon successful completion of milestones.
@app.route("/complete-challenge/<int:challenge_id>")
def complete_challenge(challenge_id):
  # Update user progress
  user.solved_challenges += 1
  user.points += 10
  db.session.commit()

  # Check if challenge completion qualifies for a badge
  if award_badge(user.id, 1):  # Badge ID for "First Steps"
    flash("Congratulations! You've earned the First Steps badge.")

  # Render user profile page with earned badges information
  return render_template("profile.html", user=user)