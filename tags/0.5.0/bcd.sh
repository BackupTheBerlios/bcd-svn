# bash utility functions for bcd
# Source this in your .bashrc

# =====================================================
# Copyright (c) Miki Tebeka <miki.tebeka@gmail.com> 
# This file is under the GNU Public License (GPL), see
# http://www.gnu.org/copyleft/gpl.html for more details
# =====================================================

# $Id$

# BCD function, call the bcd utility and change directory
bcd()
{
    output=`bcd.py $@`
    if [ -z "$output" ]; then
        return;
    elif [ -d "$output" ]; then
        cd "$output"
    else
        echo "$output"
    fi
}

# Also "Jump To"
alias jt=bcd

# Set completion
complete -C "bcd.py -c" bcd
complete -C "bcd.py -c" jt
