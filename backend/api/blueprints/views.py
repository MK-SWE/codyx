""" Blueprint module """
from flask import Blueprint

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
