# bash utility functions for bcd

# =====================================================
# Copyright (c) Miki Tebeka <miki.tebeka@zoran.com> 
# This file is under the GNU Public License (GPL), see
# http://www.gnu.org/copyleft/gpl.html for more details
# =====================================================

# $Id: bcd.sh 903 2004-09-07 14:59:41Z mikit $

bcd()
{
    dir=`bcd.py $@`
    if [ -d $dir ]; then
        cd $dir
    else
        echo "$dir: no such directory"
    fi
}

complete -C "bcd.py -c" bcd
