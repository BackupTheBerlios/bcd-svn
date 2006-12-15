# bash utility functions for bcd
# Source this in your .bashrc

# =====================================================
# Copyright (c) Miki Tebeka <miki.tebeka@gmail.com> 
# This file is under the GNU Public License (GPL), see
# http://www.gnu.org/copyleft/gpl.html for more details
# =====================================================

# $Id: bcd.sh 903 2004-09-07 14:59:41Z mikit $

# BCD function, call the bcd utility and change directory
bcd()
{
    dir=`bcd.py $@`
    if [ -d $dir ]; then
        cd $dir
    else
        echo "$dir: no such directory"
    fi
}

# Also "Jump To"
alias jt=bcd

# Set completion
complete -C "bcd.py -c" bcd
complete -C "bcd.py -c" jt
