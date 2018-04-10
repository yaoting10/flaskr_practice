#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Tim Yao'


import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE']