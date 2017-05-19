#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
[lib/lib/environment.py]

Defines the "environment" command.
"""

import os
import sys

verbs = {}

def environment(argc):
    """
       environment: Configure environment variables.

       Usage:
          environment set VARIABLE VALUE
          environment macro add REGEXP REPLACEMENT
          environment alias add COMMAND REPLACEMENT
    """

    if argc.args['set']:
        setattr(argc.env, argc.args['VARIABLE'], argc.args['VALUE'])
        if argc.args['VARIABLE'] == 'path':
            sys.path = argc.args['VALUE'].split(os.pathsep)
    
verbs["environment"] = environment