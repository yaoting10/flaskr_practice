#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

__author__ = 'Tim Yao'

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/', defaults={'page': 'index'})
@user.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)

    except TemplateNotFound:
        abort(404)