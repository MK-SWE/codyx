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

"""
User Section
"""
@auth.route('/login', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def login():
    """ Landing page route handler"""

    if current_user.is_authenticated:
        response = jsonify(
            {
                'message': 'User already logged in',
                'session_token': session.sid},
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

@auth.route('/me', methods=['GET'])
@login_required
def user_profile():
    """ User profile route handler """
    user = current_user
    return jsonify(user.to_dict()), 200

@auth.route('/edit', methods=['POST'])
@login_required
def edit_user():
    """ Edit user data route handler """
    user = current_user
    if request.method == 'POST':
        try:
            username = request.form.get('Username', None)
            email = request.form.get('Email', None)
            full_name = request.form.get('Name', None)
            password = request.form.get('Password', None)
            if username:
                user.username = username
            if email:
                user.email = email
            if full_name:
                user.full_name = full_name
            if password:
                user.password = password
            db.session.add(user)
            db.save()
            return jsonify({'user': user.to_dict(), 
                            'message': 'User data updated successfully!'}
                            ), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'error': 'Invalid request'}), 400

"""
Challenges Section
"""
@auth.route('/test', methods=['GET'])
@login_required
def test():
    """ Test route handler"""
    return jsonify({'message': 'Test route'}), 200

@auth.route('/challenges', methods=['GET'])
@login_required
def challenges():
    challenges = db.query(Challenge).all()
    return jsonify([challenge.to_dict() for challenge in challenges]), 200

@auth.route('/challenges/<id>', methods=['GET'])
@login_required
def challenge(id):
    """ Problem page route handler """
    challenge = db.query(Challenge).filter_by(id=id).first()
    return jsonify(challenge.to_dict()), 200

@auth.route('/challenges/new', methods=['POST'])
@login_required
def createChallenge():
    """ Create challenge route handler """
    if current_user.role != 'admin':
        return jsonify({'message': 'Unauthorized'}), 401
    challenge = Challenge(
        name=request.form.get('name'),
        description=request.form.get('description'),
        ex_input=request.form.get('ex_input'),
        output=request.form.get('output'),
        difficulty=request.form.get('difficulty'),
        stars=0,
        solved=0,
        _starter_function=request.form.get('starter_function'),
        examples=request.form.get('examples'),
    )
    db.session.add(challenge)
    db.save()
    return jsonify(challenge.to_dict())

@auth.route('/challenges/<id>/submit', methods=['POST'])
@login_required
def submitChallenge(id):
    """ Submit solution route handler """
    challenge = db.query(Challenge).filter_by(id=id).first()
    code = request.form.get('code')
    lang = request.form.get('lang')
    res = current_user.submit_challenge(challenge, code, lang)
    return jsonify(res), 200
