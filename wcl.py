#!/usr/bin/env python3

import sys

f = open(sys.argv[1])

lc=0
wc=0
cc=0

for line in f:
    lc +=1
    for word in line.split():
        wc+=1
    cc += len(line)

f.close()
print(lc, wc, cc)
