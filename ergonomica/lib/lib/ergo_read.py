#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
[lib/lib/ergo_read.py]

Defines the "read" command.
"""


def main(argc):
    """
    read: Read a file.

    Usage:
       read FILE
    """
    try:
        return open(argc.args['FILE'], "r").read().split("\n")
    except IOError:
        print("[ergo: IOError]: No such readable file '%s'." % (argc.args['FILE']))
