#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import environ

__author__ = 'Tim Yao'


from flask import request, Flask

app = Flask(__name__)

# with app.test_request_context('/hello', method='POST'):
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello'
#     assert request.method == 'POST'


