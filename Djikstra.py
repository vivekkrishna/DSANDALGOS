# -*- coding: utf-8 -*-
"""
Created on Sun May  7 21:12:29 2017

Djikstra

@author: vc185059
"""
import queue as qu
import copy

l=[7,37,59,82,99,115,133,165,188,197]
distances=[]
distdict={}
edgedict={}

f=open('dijkstraData.txt','r')

for i in f.readlines():
    line=i.split()
    key=int(line.pop(0))
    edges=[]
    
    for j in line:
        [v,w]=j.split(',')
        edges.append((int(w),int(v)))
    edgedict[key]=edges
    

class priorityqueue(object):
    def __init__(self,sptuple):
        self.frontier_set=[sptuple]
    def insertelement(self,tup):
        for i in range(len(self.frontier_set)):
            if tup[1]==self.frontier_set[i][1]:
                if tup[0]<self.frontier_set[i][0]:
                    del self.frontier_set[i]
                    #self.frontier_set.remove(frontier_set[i])
                    break
                else:
                    return

        if len(self.frontier_set)==0:
            self.frontier_set.append(tup)
            return
        for i in range(len(self.frontier_set)):
            if tup[0]<self.frontier_set[i][0]:
                self.frontier_set.insert(i,tup)
                return
        self.frontier_set.append(tup)
            
        
    def pop(self):
        a=self.frontier_set[0]
        del self.frontier_set[0]
        return a
    def getfrontierset(self):
        return self.frontier_set
    def size(self):
        return len(self.frontier_set)

Exploreddict={}
Exploreddict[1]=0
for i in edgedict[1]:
    (w,v)=i    
    tup=(w,v,w)
    try:
        connectededges.insertelement(tup)
    except NameError:
        connectededges=priorityqueue(tup)

while connectededges.size()>0:
    (w,v,td)=connectededges.pop()
    if v not in Exploreddict:
        Exploreddict[v]=td
    for j in edgedict[v]:
        (w1,v1)=j
        if v1 not in Exploreddict:
            connectededges.insertelement((w1+w,v1,w1+td))
            
for i in l:
    distances.append(Exploreddict[i])
    
print(distances)
        





    
        
