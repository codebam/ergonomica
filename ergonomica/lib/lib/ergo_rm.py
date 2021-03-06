#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
[lib/lib/rm.py]

Defines the "rm" command.
"""

import os
import shutil
from ergonomica.lib.lang.error import ErgonomicaError


def main(argc):
    """rm: Remove files and directories.

    Usage:
       rm FILE
    """

    _file = argc.args['FILE']
    if _file[0] == "/":
        path = _file
    elif _file[0] == "~":
        path = os.path.expanduser(_file)
    else:
        path = os.path.join(argc.env.directory, _file)

    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    else:
        raise ErgonomicaError("[ergo: NoSuchFileOrDirectoryError]: '%s'." % (path))
