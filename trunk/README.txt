==========================
"bcd" version 0.5.0 README
==========================
:Author: Miki Tebeka <miki.tebeka@gmail.com>
:Data: $Date$

.. contents::


.. Note::
    I no longer maintain BCD since I moved to linux and found
    `bash-completion`_.

    If you feel the project is useful and would like to take over, drop me_ a
    line.

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

ToDo
====
* Find someone to take over the project :)
* Add path completion - `bcd project1/l<TAB>` will complete all
  directories under /path/to/project1/l*

.. _`bash-completion`: http://www.caliban.org/bash/
.. _me: mailto:miki.tebeka@gmail.com


.. comment: vim:ft=rst spell
