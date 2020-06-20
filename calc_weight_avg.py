#!/usr/bin/env python3

import sys
fin = open(sys.argv[1])
fout=open("avg.txt",'w')
w=0
ct=0
for line in fin:
    line=line.split(",")
    ct +=1
    #weight=line[1]
    #print(line,end="")
    print(line, line[0],line[1],end="")
    if line[0] != "Date":
        w += int(line[1])

avg_weight = w/ct 

fout.write(str(avg_weight))
fout.close()
fin.close()




