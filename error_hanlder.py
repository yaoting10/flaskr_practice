#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import render_template, Flask

__author__ = 'Tim Yao'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
