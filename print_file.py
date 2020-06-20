#!/usr/bin/env python3

import sys     # we need this library to deal with operating system

filename = sys.argv[1]
infile = open(filename)
for line in infile:
    print(line,end="")
infile.close()
