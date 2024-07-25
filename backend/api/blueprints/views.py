""" Blueprint module """
from flask import Blueprint
from flask import jsonify
from utils import STORAGE
from models import Challenge

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

@views.route('/challenges')
def challenges():
    challenges = STORAGE.all(Challenge)
    challenges_list = []
    for challenge in challenges.values():
        challenge_dict = {
            'id': challenge.id,
            'name': challenge.name,
            'description': challenge.description,
            'ex_input': challenge.ex_input,
            'output': challenge.output,
            'difficulty': challenge.difficulty,
            'starterCode': challenge._starter_function,
            'examples': challenge.examples,
            'stars': challenge.stars,
            'solved': challenge.solved,
        }
        challenges_list.append(challenge_dict)
    return jsonify(challenges_list)

@views.route('/challenges/<id>')
def challenge(id):
    """ Challenge page route handler """
    # Retrieve Challenge details based on the param
    Challenge_id = Challenge.query.get(id)
    if Challenge_id:
        ChallengeDetails = {
            'id': Challenge.id,
            'name': Challenge.name,
            'description': Challenge.description,
            'examples': [
                {
                    'id': example.id,
                    'inputText': example.input_text,
                    'outputText': example.output_text,
                    'explanation': example.explanation,
                }
                for example in Challenge.examples
            ],
            'constraints': Challenge.constraints,
            '_starter_function': Challenge._starter_function,
        }
        return jsonify(ChallengeDetails)
    else:
        return jsonify({'error': 'Challenge not found'})
