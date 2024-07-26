"""Module for awarding user badges"""
from models import User
from flask import flash
from datetime import datetime

# dictionary to store badge information and corresponding milestones
# (user actions required to earn the badge).
BADGES = {
  1: {
    "name": "First Steps",
    "description": "Completed your first coding challenge",
    "milestone": lambda User: User.solved_challenges >= 1
  },
  2: {
    "name": "Code Warrior",
    "description": "Completed 10 coding challenges",
    "milestone": lambda User: User.solved_challenges >= 10
  },
  2: {
    "name": "Code Master",
    "description": "Completed 50 coding challenges",
    "milestone": lambda User: User.solved_challenges >= 50
  },
  3: {
    "name": "Code Champion",
    "description": "Completed 75 coding challenges",
    "milestone": lambda User: User.solved_challenges >= 75
  },
  4: {
    "name": "Code Ninja",
    "description": "Completed 100 coding challenges",
    "milestone": lambda User: User.solved_challenges >= 100
  },
  5: {
    "name": "Code Legend",
    "description": "Completed 150 coding challenges",
    "milestone": lambda User: User.solved_challenges >= 150
  },
  6: {
    "name": "Code God",
    "description": "Completed 200 coding challenges",
    "milestone": lambda User: User.solved_challenges >= 200
  },
  7: {
    "name": "Code King",
    "description": "Collected 100 points",
    "milestone": lambda User: User.points >= 100
  },
  8: {
    "name": "Code Overlord",
    "description": "Collected 250 points",
    "milestone": lambda User: User.collected_points >= 250
  },
  9: {
    "name": "Code Emperor",
    "description": "Collected 500 points",
    "milestone": lambda User: User.points >= 500
  },
  10: {
    "name": "Code Deity",
    "description": "Collected 750 points",
    "milestone": lambda User: User.points >= 750
  },
  11: {
    "name": "Code Divinity",
    "description": "Collected 1000 points",
    "milestone": lambda User: User.points >= 1000
  },
  12: {
    "name": "Code Immortality",
    "description": "Reached 30 days of consecutive coding",
    "milestone": lambda User: User.consecutive_days >= 30
  },

}


def award_badge(User):
  """Award a badge to a user if they have met the milestone"""
  for badge_id, badge in BADGES.items():
    if badge_id not in User.badges and badge["milestone"](User):
      User.badges.append(badge_id)
      print(f"Congratulations! You've earned the {BADGES[badge_id]['name']} badge!")
      # Save the updated user data
      User.save()


def get_user_badges(User):
  """Return a list of all badges earned by a user"""
  return [BADGES[badge_id] for badge_id in User.badges]


def get_all_badges():
  """Return a list of all available badges"""
  return BADGES.values()


def has_badge(User, badge_id):
  """Check if a user has earned a specific badge"""
  return badge_id in User.badges


def get_badge(badge_id):
  """Return a specific badge by ID"""
  return BADGES[badge_id]


def award_1st_badge(User, badge_id):
  """Award the first badge to a user"""
  if User.soloved_challenges >= 1:
    User.badges.append(badge_id)
    flash(f"Congratulations! You've earned the First Steps badge!")
    # Save the updated user data
    User.save()


  

def check_consecutive_days(User):
  """Check if a user has submitted a solution each day for the last 30 days"""
  # Get the user's submissions sorted by date
  sorted_submissions = sorted(User.submissions, key=lambda x: x.submission_date, reverse=True)
  # Check if the user has submitted a solution each day for the last 30 days
  current_date = datetime.now().date()
  consecutive_days = 0
  for submission in sorted_submissions:
    if (current_date - submission.submission_date).days <= 30:
      consecutive_days += 1
    else:
      break
  return consecutive_days
