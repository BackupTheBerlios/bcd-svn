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
from sys import platform
from ConfigParser import ConfigParser, Error as ConfigParserError
from Tkinter import *
from tkMessageBox import showerror

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

def set_selected(lb, curr):
    '''Set selected item to "curr"'''
    lb.select_clear(ACTIVE)
    lb.select_set(curr)
    lb.activate(curr)

def move(e, step):
    '''Move up/down one step'''
    lb = e.widget
    curr = (lb.index(ACTIVE) + step) % lb.size()
    set_selected(lb, curr)

def print_quit(e, root):
    '''Print directory and exit'''
    lb = e.widget
    line = lb.get(ACTIVE)
    print_path(line[line.find("]") + 2:])
    root.quit()

def edit(e):
    '''Edit the rc file and reload'''
    editor = CONFIG["editor"]
    if platform == "win32":
        devnull = "nul"
    else:
        devnull = "/dev/null"
    if not editor:
        showerror("No Editor", "No editor is configured. Try setting "
                               "BCD_EDITOR environment variable")
        return
    try:
        cmd = "%s %s > %s 2>&1" % (editor, rcfile, devnull)
        system(cmd)
    except OSError:
        showerror("Editor Problem", "Error running editor")
        return
    reload(e.widget)

def reload(lb, prefix=""):
    '''Load rc file to control'''

    load_rc()
    lb.delete(0, END)

    if not ALIASES:
        return
    # Max length of alias
    max_alias = max([len(alias) for alias, path in ALIASES])
    for alias, path in ALIASES:
        if alias.startswith(prefix):
            lb.insert(END, "[%-*s] %s" % (max_alias, alias, path))
    lb.pack(fill=BOTH, expand=1)
    set_selected(lb, 0)

def launch_ui(args):
    # Window settings
    font = (CONFIG["font"], CONFIG["font_size"])
    bg = CONFIG["background"]
    fg = CONFIG["foreground"]

    root = Tk() # Main window
    root.title("BCD 0.2.0")

    files = Listbox(root, font=font, bg=bg, fg=fg)
    if args:
        prefix = args[0]
    else:
        prefix = ""
    reload(files, prefix)

    # Can't find prefix, load all
    if prefix and (files.size() == 0):
        prefix = ""
        reload(files, "")

    # Bind some keystrokes
    files.bind("<Escape>", lambda e: root.quit()) # ESC will quit
    files.bind("<Return>", lambda e: print_quit(e, root)) # Enter will select
    files.bind("e", edit) # "e" will edit
    files.bind("r", lambda e: load(files, "")) # "r" will reload all

    # vi like movement
    files.bind("k", lambda e: move(e, -1)) # "k" is up
    files.bind("j", lambda e: move(e, 1)) # "j" is down
    files.bind("q", lambda e: root.quit()) # "q" will quit

    # Help
    help = Label(root, font=font, bg=bg, fg=fg,
            text="<UP>/k = up, <DOWN>/j = down, e = Edit, <ESC>/q = quit")
    help.pack(fill="both")

    files.focus()

    # Run GUI
    root.mainloop()

def main(argv = None):
    global RCFILE

    if argv is None:
        import sys
        argv = sys.argv

    from optparse import OptionParser

    # Command line parsing
    p = OptionParser("usage: %prog [options] [ALIAS]")
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

    # Not found or no arguments, show GUI
    try:
        launch_ui(args)
    except TclError, e:
        raise SystemExit("bcd: error: %s" % e)

if __name__ == "__main__":
    main()
