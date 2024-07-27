""" Create tests for the badges system. """
from flask import Blueprint, jsonify, request
from backend.models import User
from backend import db
from backend.api import app
from backend.badges.badges import BADGES, award_badge, get_badges, has_badge, get_badge, get_all_badges
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


# Test the API routes
class TestBadgeAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_badges(self):
        """Tests the GET /badges route."""
        response = self.app.get("/badges")
        data = response.get_json()

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), len(BADGES))

    def test_award_badge(self):
        """Tests the POST /badges/award route."""
        user = User([])
        db.session.add(user)
        db.session.commit()

        # Data to send with the request
        data = {"user_id": user.id, "badge_id": 1}

        response = self.app.post("/badges/award", json=data)
        user = User.query.get(user.id)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertTrue(1 in user.badges)

    def test_get_user_badges(self):
        """Tests the GET /badges/user/<user_id> route."""
        user = User([1, 2, 3])
        db.session.add(user)
        db.session.commit()

        response = self.app.get(f"/badges/user/{user.id}")
        data = response.get_json()

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), len(user.badges))

    def test_check_user_badge(self):
        """Tests the GET /badges/user/<user_id>/<badge_id> route."""
        user = User([1, 2, 3])
        db.session.add(user)
        db.session.commit()

        response = self.app.get(f"/badges/user/{user.id}/1")
        data = response.get_json()

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data)

    def test_get_specific_badge(self):
        """Tests the GET /badges/<badge_id> route."""
        badge_id = 1
        response = self.app.get(f"/badges/{badge_id}")
        data = response.get_json()

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], BADGES[badge_id]["name"])

    # Docstring test (using a custom decorator)
    @unittest.skipIf(not award_badge.__doc__, "Function has no docstring")
    def test_award_badge_docstring(self):
        """Tests if the `award_badge` function has a docstring."""
        self.assertIsNotNone(award_badge.__doc__)


    # Docstring test (using a custom decorator)
    @unittest.skipIf(not get_badges.__doc__, "Function has no docstring")
    def test_get_badges_docstring(self):
        """Tests if the `get_badges` function has a docstring."""
        self.assertIsNotNone(get_badges.__doc__)
    
    # Docstring test (using a custom decorator)
    @unittest.skipIf(not has_badge.__doc__, "Function has no docstring")
    def test_has_badge_docstring(self):
        """Tests if the `has_badge` function has a docstring."""
        self.assertIsNotNone(has_badge.__doc__)

    # Docstring test
    def test_get_badge_docstring(self):
        """Tests if the `get_badge` function has a docstring."""
        self.assertIsNotNone(get_badge.__doc__)

    # Docstring test
    def test_get_all_badges_docstring(self):
        """Tests if the `get_all_badges` function has a docstring."""
        self.assertIsNotNone(get_all_badges.__doc__)
    
    # Docstring test
    def test_award_badge_docstring(self):
        """Tests if the `award_badge` function has a docstring."""
        self.assertIsNotNone(award_badge.__doc__)
    
    # Docstring test
    def test_get_badges_docstring(self):
        """Tests if the `get_badges` function has a docstring."""
        self.assertIsNotNone(get_badges.__doc__)
    
    # Docstring test
    def test_get_all_badges_docstring(self):
        """Tests if the `get_all_badges` function has a docstring."""
        self.assertIsNotNone(get_all_badges.__doc__)




# Run the tests
if __name__ == '__main__':
    unittest.main()
