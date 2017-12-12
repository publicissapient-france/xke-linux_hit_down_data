#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python 3

import sys

if __name__ == "__main__":
    received= sys.argv[1].upper().split(',')
    response= ["LE PORT","PEYNIER","CHATEAUNEUF-LE-ROUGE","ROUSSET","AGEN","BOURG-LA-REINE","SIX-FOURS-LES-PLAGES","MERICOURT"]
    if received in response:
        print("True")
    else:
        print("False")

