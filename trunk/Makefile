# Makefile for "bcd" project
 
# =====================================================
# Copyright (c) Miki Tebeka <miki.tebeka@zoran.com> 
# This file is under the GNU Public License (GPL), see
# http://www.gnu.org/copyleft/gpl.html for more details
# =====================================================

# Miki Tebeka <miki.tebeka@zoran.com>

# $Id$

# You'll need the following tools:
# Python - http://www.python.org
# py2exe - http://starship.python.net/crew/theller/py2exe
#
# Just type "bin\make" on a DOS console (or "make" on cygwin shell)
 
 
DIST = bcd
ZIP = bcd.zip
WZIP = bcdw32.zip
SRCZIP = bcdsrc.zip

SOURCES = Makefile \
		  bcd.bat \
		  bcd.py \
		  bcd.sh \
		  pyexe.py \
		  se \
		  setup.py

DOCS = bcdrc_example \
	   README.txt

ifeq ($(OSTYPE),cygwin)
	PYTHON = ${shell cygpath -au `cmd /c pyexe.py`}
else
	PWD = ${shell cmd /c cd}
	PATH := $(PWD)\bin;$(PATH)
	PYTHON = $(shell cmd /c pyexe.py)
endif

all:
	@echo Try either \"dist\" or \"w32dist\" targets
	@echo

initial:
	rm -fr $(DIST)
	mkdir $(DIST)
	cp $(DOCS) $(DIST)

dist: $(ZIP)

$(ZIP): initial bcd.py bcd.sh $(DOCS)
	cp bcd.py $(DIST)
	cp bcd.sh $(DIST)
	zip -r9 $(ZIP) $(DIST)

w32dist: $(WZIP)

$(WZIP): initial bcd.py bcd.bat setup.py $(DOCS)
	$(PYTHON) setup.py py2exe -d $(DIST)
	mv $(DIST)/bcd.exe $(DIST)/bcdw.exe
	cp bcd.bat $(DIST)
	zip -r9 $(WZIP) $(DIST)

srcdist: $(SRCZIP)

$(SRCZIP): initial $(SOURCES)
	cp -r $(SOURCES) $(DIST)
	rm -fr $(DIST)/bin/.svn
	zip -r9 $(SRCZIP) $(DIST)

clean:
	rm -fr $(DIST)
	rm -fr build
	rm -fr $(ZIP) $(WZIP) $(SRCZIP)

.PHONY: all dist w32dist clean srcdist initial
