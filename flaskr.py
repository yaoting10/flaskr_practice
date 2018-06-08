#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask.json import jsonify


__author__ = 'Tim Yao'

from flask import render_template, g, app, Flask
from com.controller.users_page import user

from database import engine, db_session, cache, init_db

app = Flask(__name__)
app.config['USERNAME'] = 'admin'
app.config['PASSWORD'] = 'admin'
app.config['SECRET_KEY'] = '123'
app.register_blueprint(user, url_prefix='/user')


@app.route('/<model>/')
def show_entries(model):
    cur = engine.execute('select title, text from entry order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return 'No entries here so far'
    # return render_template("show_entries.html", entries=entries)





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