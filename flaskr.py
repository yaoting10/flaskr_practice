#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask.json import jsonify

__author__ = 'Tim Yao'

from com.util.JsonUtil import to_json, json_to_dict
from flask import Flask, json, session, abort, request, flash, url_for, redirect

from flask import render_template, g, app, Flask

from com.orm.models import User, Entries
from database import engine, db_session, cache, init_db

app = Flask(__name__)
app.config['USERNAME'] = 'admin'
app.config['PASSWORD'] = 'admin'
app.config['SECRET_KEY'] = '123'


@app.route('/')
def show_entries():
    cur = engine.execute('select title, text from entry order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return 'No entries here so far'
    # return render_template("show_entries.html", entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    engine.execute(
        "INSERT INTO entry ( title, text) values ( %s, %s)", (request.form['title'], request.form['text'])
    )
    db_session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


@app.route('/redirect_to')
def redirect_to():
    flash('New entry was successfully posted')
    return redirect('/redirect_error')


@app.route('/redirect_error')
def redirect_error():
    abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]


@app.context_processor
def utility_processor():
    def format_price(amount, currency=u'¥'):
        return u'{0:.3f}{1}'.format(amount, currency)
    return dict(format_price=format_price)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)