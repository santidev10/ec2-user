#!/usr/bin/env python


def average(lis):
    ct=0
    numtot=0
    for num in lis:
        ct +=1
        numtot= numtot + num
    print("average: ", numtot/ct)
    return numtot/ct 

list=[1,2,3,4,5,6]
print(average(list))
