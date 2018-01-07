#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python 3

import sys

if __name__ == "__main__":
    inputData = sys.argv[1].upper()
    if "jq" in inputData and ".uri" in inputData and "*" in inputData:
        print("True")
    else:
        print("False")

