# pylint: disable=W0603
"""
[verbs.py]

Contains all the native commands for ergonomica
"""

import os
import fnmatch

run = True
directory = "/"

verbs = {}

def yes(args, kwargs):
    """
     Returns a 'y'
    """
    return "y"

verbs["yes"] = yes

def Quit(args, kwargs):
    """Quits the ergonomica shell."""
    global run
    run = False

verbs["quit"] = Quit

def Help(args):
    """Display all commands"""
    if len(args[0]) == 0:
        print "test"
    else:
        print args

verbs["help"] = Help

def cd(args, kwargs):
    """Changes to a directory"""
    global directory
    directory = args[0]

verbs["cd"] = cd

def ls(args, kwargs):
    """List files in a directory."""
    if len(args) == 0:
        return os.listdir(directory)
    else:
        return os.listdir(args[0])

verbs["ls"] = ls

def find(args, kwargs):
    """Finds a file with a pattern"""
    pattern = kwargs["name"]
    path = args[0]
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

verbs["find"] = find

def echo(args, kwargs):
    """Echos a phrase"""
    return args[0]

verbs["echo"] = find
verbs["print"] = find

def clear(args, kwargs):
    """Clears the screen"""
    os.system('clear')

verbs["clear"] = clear
