#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import environ

__author__ = 'Tim Yao'

from flask import Flask, url_for, request, render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username


# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id


# @app.route('/projects/')
# def projects():
#     return 'The project page'


@app.route('/')
def index(): return "hello"


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        f = request.files['the_file']
        f.save('/Users/Tim/work/PycharmProjects/flaskr/uploaded_file.txt')
        print(request.method)
    else:
        print("GET")
    return "login"


@app.route('/user/<username>')
def profile(username): return "ok"


# with app.test_request_context():
#     print(url_for('index'))
    # print(url_for('login'))
    # print(url_for('login', next='/'))
    # print(url_for('profile', username='John Doe'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
