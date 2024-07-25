#!/usr/bin/python3
""" Guidy Blueprint """

import re
from flask import *
from flask_cors import cross_origin
from backend.models.user import User
from backend.models.admin import Admin
from backend.models.challenge import Challenge
from backend.utils import STORAGE as db
from flask_login import (
    LoginManager, current_user, login_user, login_required, logout_user
)

auth = Blueprint('auth', __name__)
Manager = LoginManager()


@Manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@auth.route('/login', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def login():
    """ Landing page route handler"""

    if current_user.is_authenticated:
        response = jsonify(
            {
                'message': 'User already logged in',
                'session_id': current_user.session_token
                },
            ), 200
        return make_response(response)

    if request.method == 'POST':

        identity = request.form.get('Username', None)
        password = request.form.get('Password', None)

        if not identity or not password:
            return jsonify({'error': 'Invalid credentials'}), 401

        if '@' in identity and '.' in identity and identity[-1] != '.':
            user = db.query(User).filter_by(email=identity).first()
        else:
            user = db.query(User).filter_by(username=identity).first()

        if user is not None and user.check_password(password):
            login_user(user)
            user.authenticated = True
            db.session.add(user)
            db.save()
            return jsonify({'user': user.to_dict()}), 200
        else:
            return jsonify({
                'error': 'Invalid credentials',
                'message': 'User not found'
                }), 401
    return jsonify({'error': 'Invalid request'}), 400


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """ Register page route handler"""

    if request.method == 'POST':
        try:
            username = request.form.get('Username', None)
            user = db.query(User).filter_by(username=username).first()

            if user is not None:
                return jsonify({'error': f'User {user.username} already exists'}), 409

            email = request.form.get('Email', None)
            full_name = request.form.get('Name', None)
            password = request.form.get('Password', None)
            user = User(username=username, email=email,
                        full_name=full_name, password=password)
            db.session.add(user)
            db.save()
            return jsonify({'user': user.to_dict(), 
                            'message': f'User {str(user.username)} created successfully!'}
                           ), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    return jsonify({'error': 'Invalid request'}), 400

@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    """ Logout page route handler"""
    user = current_user
    if current_user is None:
        return jsonify({'error': 'You Are Not Logged In.'}), 404
    
    if user.is_authenticated:
        user.authenticated = False
        session.clear()
        logout_user()
        response = jsonify({'message': f'User logged out successfully!'}), 200
        db.save()
        return make_response(response)

@auth.route('/test', methods=['GET'])
@login_required
def test():
    """ Test route handler"""
    return jsonify({'message': 'Test route'}), 200

@auth.route('/challenges', methods=['GET'])
@login_required
def problems():
    challenges = db.query(Challenge).all()
    return jsonify(challenges), 200

@auth.route('/challenges/<param>', methods=['GET'])
def problem(param):
    """ Problem page route handler """
    # TODO: Retrieve problem details based on the param
    problemDetails = {
        'id': 1,
        'title': "1. Two Sum",
        'problemStatement': "<p>\n  Given an array of integers <code>nums</code> and an integer <code>target</code>, return\n  <em>indices of the two numbers such that they add up to</em> <code>target</code>.\n</p>\n<p>\n  You may assume that each input would have <strong>exactly one solution</strong>, and you\n  may not use thesame element twice.\n</p>\n<p>You can return the answer in any order.</p>",
        'examples': [
            {
                'id': 1,
                'inputText': "nums = [2,7,11,15], target = 9",
                'outputText': "[0,1]",
                'explanation': "Because nums[0] + nums[1] == 9, we return [0, 1].",
            },
            {
                'id': 2,
                'inputText': "nums = [3,2,4], target = 6",
                'outputText': "[1,2]",
                'explanation': "Because nums[1] + nums[2] == 6, we return [1, 2].",
            },
            {
                'id': 3,
                'inputText': " nums = [3,3], target = 6",
                'outputText': "[0,1]",
            },
        ],
        'constraints': "<li'>\n  <code>2 ≤ nums.length ≤ 10</code>\n</li> <li>\n<code>-10 ≤ nums[i] ≤ 10</code>\n</li> <li>\n<code>-10 ≤ target ≤ 10</code>\n</li>\n<li>\n<strong>Only one valid answer exists.</strong>\n</li>",
        'starterCode': "function twoSum(nums, target) {\n  // Your code here\n}",
    }
    return jsonify(problemDetails)

@auth.route('/submit', methods=['POST'])
@login_required
def submit():
    """ Submit page route handler """
    print(request.get_json())
    return "<h1>Welcome to CodyX submit page</h1>"
