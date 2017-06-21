# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:14:17 2017

2-sum

@author: vc185059
"""

f=open('2sum.txt','r')

sums=set()

arset=set()
for i in f.readlines():
    a=int(i)
    arset.add(a)

count=0

for t in range(-10000,10001):
    for x in arset:
        if t-x==x:
            continue
        if t-x in arset:
            count+=1
            break

print(count)