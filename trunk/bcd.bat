@echo off

rem Batch file to call bcd.py

rem =====================================================
rem Copyright (c) Miki Tebeka <miki.tebeka@zoran.com> 
rem This file is under the GNU Public License (GPL), see
rem http://www.gnu.org/copyleft/gpl.html for more details
rem =====================================================

rem Miki Tebeka <miki.tebeka@zoran.com>
rem $Id: bcd.py 898 2004-08-31 11:49:52Z mikit $

if "%1" == "-h" goto HELP

set tmp_script=%TEMP%\bcd_tmp.bat
bcdw.exe -w %1 > %tmp_script%

rem Since we don't use "call" any line after the next *won't* be called
%tmp_script%

:HELP
bcdw -h
