==========================
"bcd" version 0.5.0 README
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
directory. Otherwise all the aliases will be printed to screen.

On Unix systems hitting "TAB" after bcd will complete all aliases (at least on
bash).

Configuration File
==================
The configuration file has the following syntax:

::
    work = $HOME/work
    download = $HOME/downloads
    cool_project = /mnt/cool_project

See the bcdrc_example for more details

Environment Variables
=====================
BCDRC is the location of the configuration file (otherwise it's $HOME/.bcd).

Downloading etc
===============
See http://developer.berlios.de/projects/bcd/ 


.. comment: vim:ft=rst spell
