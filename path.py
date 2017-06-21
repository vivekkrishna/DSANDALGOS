# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 15:51:51 2017

@author: vc185059
"""

a=int(input())

grid=[]
for i in range(a):
    b=list(input())
    grid.append(b)
    
#print(grid)
c=input().split()

start=(int(c[0]),int(c[1]))
end=(int(c[2]),int(c[3]))

aset=set()

def getneighbors(loc):
    global aset
    loca=loc[0]
    presentpath=loc[1]
    neighbors=[]
    for i in range(max(loca[0]-1,0),min(loca[0]+2,a)):
        for j in range(max(loca[1]-1,0),min(loca[1]+2,a)):
            try:
                if grid[i][j]=='.' and (i,j) is not loca and (i,j) not in aset and (i==loca[0] or j==loca[1]):
                    neighbors.append(((i,j),presentpath+[(i,j)]))
                    aset.add((i,j))
            except IndexError:
                continue
    return neighbors
    #print(neighbors)
                

from queue import *

q=Queue(maxsize=0)

path=[start]
q.put((start,path))




while not q.empty():
    d=q.get()
    aset.add(d[0])
    if d[0]==end:
        path=d[1]
        prev=path[0]
        finalpath=[prev]
        if path[1][0]==path[0][0]:
            prevxchanged=False
        else:
            prevxchanged=True
        for i in range(2,len(path)):
            if path[i][0]==path[i-1][0]:
                xchanged=False
                ychanged=True
            else:
                xchanged=True
                ychanged=False
                
            if not prevxchanged==xchanged:
                finalpath.append(path[i-1])
            prevxchanged=xchanged
            prevychanged=ychanged
        print(len(finalpath))
        break
    neighbors=getneighbors(d)
    for i in neighbors:
        q.put(i)
    
    