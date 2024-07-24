""" Blueprint module """
from flask import Blueprint, jsonify, request

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
        },
        {
            'id': "reverse-linked-list",
            'title': "Reverse Linked List",
            'difficulty': "Hard",
            'category': "Linked List",
            'order': 2,
        },
        {
            'id': "jump-game",
            'title': "Jump Game",
            'difficulty': "Medium",
            'category': "Dynamic Programming",
            'order': 3,
        }
    ]
    return jsonify(problemsList)
@views.route('/problems/<param>')
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

@views.route('/submit', methods=['POST'])
def submit():
    """ Submit page route handler """
    print(request.get_json())
    return "<h1>Welcome to CodyX submit page</h1>"