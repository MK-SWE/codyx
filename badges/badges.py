from models import User
from datetime import datetime
# dictionary to store badge information and corresponding milestones
# (user actions required to earn the badge).
BADGES = {
  1: {
    "name": "First Steps",
    "description": "Completed your first coding challenge",
    "milestone": lambda user: user.solved_challenges >= 1
  },
  2: {
    "name": "Code Warrior",
    "description": "Completed 10 coding challenges",
    "milestone": lambda user: user.solved_challenges >= 10
  },
  2: {
    "name": "Code Master",
    "description": "Completed 50 coding challenges",
    "milestone": lambda user: user.solved_challenges >= 50
  },
  3: {
    "name": "Code Champion",
    "description": "Completed 75 coding challenges",
    "milestone": lambda user: user.solved_challenges >= 75
  },
  4: {
    "name": "Code Ninja",
    "description": "Completed 100 coding challenges",
    "milestone": lambda user: user.solved_challenges >= 100
  },
  5: {
    "name": "Code Legend",
    "description": "Completed 150 coding challenges",
    "milestone": lambda user: user.solved_challenges >= 150
  },
  6: {
    "name": "Code God",
    "description": "Completed 200 coding challenges",
    "milestone": lambda user: user.solved_challenges >= 200
  },
  7: {
    "name": "Code King",
    "description": "Collected 100 points",
    "milestone": lambda user: user.points >= 100
  },
  8: {
    "name": "Code Overlord",
    "description": "Collected 250 points",
    "milestone": lambda user: user.collected_points >= 250
  },
  9: {
    "name": "Code Emperor",
    "description": "Collected 500 points",
    "milestone": lambda user: user.points >= 500
  },
  10: {
    "name": "Code Deity",
    "description": "Collected 750 points",
    "milestone": lambda user: user.points >= 750
  },
  11: {
    "name": "Code Divinity",
    "description": "Collected 1000 points",
    "milestone": lambda user: user.points >= 1000
  },
  12: {
    "name": "Code Immortality",
    "description": "Reached 30 days of consecutive coding",
    "milestone": lambda user: user.consecutive_days >= 30
  },

}

# Function to check if a user has earned any new badges
def award_badge(user):
  for badge_id, badge in BADGES.items():
    if badge_id not in user.badges and badge["milestone"](user):
      user.badges.append(badge_id)
      print(f"Congratulations! You've earned the {badge['name']} badge!")
      # Save the updated user data
      user.save()
