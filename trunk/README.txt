==========================
"bcd" version 0.2.0 README
==========================
:Author: Miki Tebeka <miki.tebeka@gmail.com>
:Data: $Date$

.. contents::

What is "bcd" 
=============
"bcd" stand for "Better CD". It is a "cd" replacement in the spirit of "cdargs"
(http://www.skamphausen.de/software/cdargs/).

"bcd" allows you to give symbolic names (aliases) to directories and then "cd"
to these directories.

Installation
============
Just unzip the zip file to a directory and place it in your path.
Unix users will want to add the line "source /path/to/bcd/.bcd.sh" to their
.bashrc

Running
=======
Just run "bcd" [alias]. If there is the alias is matched exactly you'll change
directory. Otherwise the bcd window will open and after selecting the right
path you will cd to there.

On Unix systems hitting "TAB" after bcd will complete all aliases (at least on
bash).

Configuration File
==================
The configuration file contains one alias and path per line.
Lines starting with '#' are ignored.

User Interface
==============
Up arrow/"k" will move up the directory list.
Down arrow/"j" will move down the directory list.
ESC/"q" will quit.
"e" will invoke the editor on the configuration file.
ENTER will select the current directory.
"r" will reload the configuration file.

Environment Variables
=====================
BCDRC is the location of the configuration file (otherwise it's $HOME/.bcd).
EDITOR, VISUAL are the name of the editor to invoke if not specified in the
configuration file.

On windows systems the editor default to notepad.
