#!/usr/bin/env python
'''Tkinter replacement to cdargs utility'''

# =====================================================
# Copyright (c) Miki Tebeka <miki.tebeka@gmail.com> 
# This file is under the GNU Public License (GPL), see
# http://www.gnu.org/copyleft/gpl.html for more details
# =====================================================

__author__ = "Miki Tebeka <miki.tebeka@gmail.com>"
__version__ = "0.5.0"

from user import home
from os.path import join, isfile, expandvars
from os import environ, system
from sys import platform, stderr
from ConfigParser import ConfigParser, Error as ConfigParserError

ALIASES = []

def rc_filename():
    if "BCDRC" in environ:
        return environ["BCDRC"]

    if platform == "win32":
        prefix = "_"
    else:
        prefix = "."
    return join(home, prefix + "bcdrc")

def load_rc(filename):
    aliases = {}
    for line in open(filename):
        line = line.strip()
        if (not line) or line[0] == "#":
            continue
        name, path = line.split("=", 1)
        name = name.strip()
        path = path.strip()

        aliases[name] = path

    return aliases

def print_path(path):
    path = expandvars(path)
    if platform == "win32":
        print "@echo off"
        print "cd /d %s" % path
    else:
        print path

def main(argv = None):

    if argv is None:
        import sys
        argv = sys.argv

    from optparse import OptionParser

    # Command line parsing
    p = OptionParser("usage: %prog [options] [ALIAS]", 
        version="bcd " + __version__)
    p.add_option("-c", help="compelte alias", dest="complete", default=0,
             action="store_true")

    opts, args = p.parse_args()
    if (not opts.complete) and (len(args) not in (0, 1)):
        p.error("wrong number of arguments") # Will exit

    rcfile = rc_filename()

    if not isfile(rcfile):
        raise SystemExit("can't find initialization file %s" % rcfile)

    try:
        # Initial load of rc file
        aliases = load_rc(rcfile)
    except (IOError, ConfigParserError, ValueError), e:
        raise SystemExit("bcd: %s: error: %s" % (rcfile, e))

    # Print all aliases starting with argument
    if opts.complete:
        if args:
            prefix = args[1]
        else:
            prefix = "" # string.startswith("") is always true
        for alias in aliases:
            if alias.startswith(prefix):
                print alias
        raise SystemExit

    # Try to find given alias
    if args:
        path = aliases.get(args[0], None)
        if path:
            print_path(path)
            raise SystemExit

    # Not found or no arguments, show all options
    # We print to stderr so it won't be caught but the wrapping function
    max_alias_length = max([len(a[0]) for a in aliases])
    padding = 5
    for alias, path in sorted(aliases.items()):
        line = "-" * (max_alias_length + padding - len(alias))
        print >> stderr, "%s %s %s" % (alias, line, path)

    if args: # Didn't find
        raise SystemExit("error: can't find %s" % args[0])

if __name__ == "__main__":
    main()
