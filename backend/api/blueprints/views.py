""" Blueprint module """
from flask import Blueprint
from flask import jsonify

views = Blueprint('views', __name__)

@views.route('/')
def index():
    """ Landing page route handler """
    return "<h1>Welcome to CodyX landing page</h1>"

@views.route('/about')
def about():
    """ About page route handler """
    return "<h1>Welcome to CodyX about page</h1>"

@views.route('/contact')
def contact():
    """ Contact page route handler """
    return "<h1>Welcome to CodyX contact page</h1>"

@views.route('/terms')
def terms():
    """ Terms page route handler """
    return "<h1>Welcome to CodyX terms page</h1>"

@views.route('/privacy')
def privacy():
    """ Privacy page route handler """
    return "<h1>Welcome to CodyX privacy page</h1>"
    
@views.route('/problems')
def problems():
    problemsList = [
        {
            'id': "twoSum",
            'title': "Two Sum",
            'difficulty': "Easy",
            'category': "Array",
            'order': 1,
            'videoId': "8-k1C6ehKuw",
        },
        {
            'id': "reverse-linked-list",
            'title': "Reverse Linked List",
            'difficulty': "Hard",
            'category': "Linked List",
            'order': 2,
            'videoId': "",
        },
        {
            'id': "jump-game",
            'title': "Jump Game",
            'difficulty': "Medium",
            'category': "Dynamic Programming",
            'order': 3,
            'videoId': "",
        }
    ]
    return jsonify(problemsList)