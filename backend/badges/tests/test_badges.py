""" Create rests for the badges system. """
from flask import Blueprint, jsonify, request
from backend.models import User
from backend import db
from backend.badges.badges import BADGES, award_badge, get_badges, has_badge, get_badge
import unittest


class TestAwardBadge(unittest.TestCase):

    def test_award_badge_success(self):
        """Tests awarding a badge to a user who doesn't have it."""
        user = User([])
        badge_name = "Gold Star"

        # Call the function
        awarded_badge = award_badge(user, badge_name)

        # Assertions
        self.assertTrue(badge_name in user.badges)
        self.assertEqual(awarded_badge, badge_name)

    def test_award_badge_duplicate(self):
        """Tests awarding a badge a user already has."""
        user = User(["Gold Star"])
        badge_name = "Gold Star"

        # Call the function
        awarded_badge = award_badge(user, badge_name)

        # Assertions
        self.assertFalse(badge_name in user.badges)  # User doesn't get another badge
        self.assertIsNone(awarded_badge)  # No badge awarded

    def test_award_badge_invalid_badge(self):
        """Tests awarding a non-existent badge."""
        user = User([])
        badge_name = "Non-existent Badge"

        # Call the function (may raise an exception)
        with self.assertRaises(ValueError):
            award_badge(user, badge_name)

    # Docstring test (using a custom decorator)
    @unittest.skipIf(not award_badge.__doc__, "Function has no docstring")
    def test_award_badge_docstring(self):
        """Tests if the `award_badge` function has a docstring."""
        self.assertIsNotNone(award_badge.__doc__)
        # You can add further checks to the docstring content here

badges = Blueprint("badges", __name__)

@badges.route("/badges", methods=["GET"])
def get_badges():
    return jsonify(BADGES)

@badges.route("/badges/award", methods=["POST"])
def award_badge():
    data = request.get_json()
    user = User.query.get(data["user_id"])
    badge_id = data["badge_id"]
    award_badge(user, badge_id)
    return jsonify({"message": "Badge awarded successfully"})

@badges.route("/badges/user/<int:user_id>", methods=["GET"])
def get_user_badges(user_id):
    user = User.query.get(user_id)
    return jsonify(get_badges(user))

@badges.route("/badges/user/<int:user_id>/<int:badge_id>", methods=["GET"])
def check_user_badge(user_id, badge_id):
    user = User.query.get(user_id)
    return jsonify(has_badge(user, badge_id))

@badges.route("/badges/<int:badge_id>", methods=["GET"])
def get_specific_badge(badge_id):
    return jsonify(get_badge(badge_id))


# Run the tests
if __name__ == '__main__':
    unittest.main()