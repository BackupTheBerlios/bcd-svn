#!/usr/bin/env python
'''Tkinter replacement to cdargs utility'''

# =====================================================
# Copyright (c) Miki Tebeka <miki.tebeka@gmail.com> 
# This file is under the GNU Public License (GPL), see
# http://www.gnu.org/copyleft/gpl.html for more details
# =====================================================

__author__ = "Miki Tebeka <miki.tebeka@gmail.com>"

# Imports
from user import home
from os.path import join, isfile, expandvars
from os import environ, system
from sys import platform, stderr
from ConfigParser import ConfigParser, Error as ConfigParserError

CONFIG = {}
ALIASES = []
RCFILE = ""

def rc_filename():
    # Check for rc file
    if "BCDRC" in environ:
        return environ["BCDRC"]
    else:
        if platform == "win32":
            prefix = "_"
        else:
            prefix = "."
        return join(home, prefix + "bcdrc")

def default_editor():
    '''Try to find default editor'''
    for var in ("EDITOR", "VISUAL"):
        if var in environ:
            return environ[var]
    if platform == "win32":
        windir = environ["WINDIR"]
        return join(windir, "system32", "notepad.exe")
    
    return "" # Not found

def load_rc():
    '''Load rc file'''

    cp = ConfigParser()
    cp.readfp(open(RCFILE))
    cfg = "config"
    if cp.has_section(cfg):
        for opt in cp.options(cfg):
            value = cp.get(cfg, opt)
            if opt == "font_size":
                value = int(value)
            CONFIG[opt] = value

    # Get editor from env
    if "editor" not in CONFIG:
        CONFIG["editor"] = default_editor()

    alias = "aliases"
    del ALIASES[:]
    if cp.has_section(alias):
        for opt in cp.options(alias):
            ALIASES.append((opt, cp.get(alias, opt)))

def find_path(name):
    for alias, path in ALIASES:
        if alias == name:
            return path

def print_path(path):
    path = expandvars(path)
    if platform == "win32":
        print "@echo off"
        print "cd /d %s" % path
    else:
        print path

def main(argv = None):
    global RCFILE

    if argv is None:
        import sys
        argv = sys.argv

    from optparse import OptionParser

    # Command line parsing
    p = OptionParser("usage: %prog [options] [ALIAS]", 
        version="bcd 0.4.1")
    p.add_option("-c", help="compelte alias", dest="complete", default=0,
             action="store_true")

    opts, args = p.parse_args()
    if (not opts.complete) and (len(args) not in (0, 1)):
        p.error("wrong number of arguments") # Will exit

    RCFILE = rc_filename()

    if not isfile(RCFILE):
        raise SystemExit("can't find initialization file %s" % rcfile)

    try:
        # Initial load of rc file
        load_rc()
    except (IOError, ConfigParserError, ValueError), e:
        raise SystemExit("bcd: %s: error: %s" % (rcfile, e))


    # Print all aliases starting with argument
    if opts.complete:
        if args:
            prefix = args[1]
        else:
            prefix = "" # string.startswith("") is always true
        for alias, path in ALIASES:
            if alias.startswith(prefix):
                print alias
        raise SystemExit

    # Try to find given alias
    if args:
        path = find_path(args[0])
        if path:
            print_path(path)
            raise SystemExit

    # Not found or no arguments, show all options
    # We print to stderr so it won't be caught but the wrapping function
    max_alias_length = max([len(a[0]) for a in ALIASES])
    padding = 5
    for alias, path in sorted(ALIASES):
        line = "-" * (max_alias_length + padding - len(alias))
        print >> stderr, "%s %s %s" % (alias, line, path)

    if args: # Didn't find
        raise SystemExit("error: can't find %s" % args[0])

if __name__ == "__main__":
    main()
