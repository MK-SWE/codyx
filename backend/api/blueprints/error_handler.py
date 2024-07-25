#!/usr/bin/python3
""" Blueprint module """
from flask import Blueprint
from flask import jsonify

errors = Blueprint('error', __name__)

@errors.app_errorhandler(404)
def page_not_found(error):
    return jsonify({'error': 'Not found'}), 404

@errors.app_errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

@errors.app_errorhandler(403)
def forbidden(error):
    return jsonify({'error': 'Forbidden'}), 403

@errors.app_errorhandler(401)
def unauthorized(error):
    return jsonify({'error': 'Unauthorized, Please Log In first.'}), 401
