#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask.json import jsonify

__author__ = 'Tim Yao'

from com.util.JsonUtil import to_json, json_to_dict
from flask import Flask, json

from flask import render_template, g, app, Flask

from com.orm.models import User, Entries
from database import engine, db_session, cache

app = Flask(__name__)


@app.route('/')
def show_entries():
    r = engine.execute('select * from entry e left join user u on e.id =u.id')
    print(list(r))

    d = engine.execute('select * from entry where id = 1').first()
    print(dict(d).get("title"))
    return "native sql"


@app.route('/add')
def add_entries():
    entries = User.query.filter_by(id=1).first()
    print(entries.id)
    e = Entries("title2", "text2")
    u = User('admin3')
    db_session.add(e)
    db_session.add(u)
    db_session.commit()
    return "mapper SQL"


@app.route('/cache')
def get_cache():
    ticket = cache.get("2c9284915e0e9d34015e0ea082730006").decode('utf-8')
    print(json_to_dict(ticket).get("roleName"))
    return "cache redis"

# @app.teardown_request
# def shutdown_session(exception=None):
#     db_session.remove()



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)