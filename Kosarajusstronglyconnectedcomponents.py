# -*- coding: utf-8 -*-
"""
Created on Wed May  3 07:41:00 2017

@author: vc185059
"""

from operator import itemgetter

f=open('SCC.txt','r')
edgelist=[]
graphdict={}
reversegraphdict={}
maxvertex=0
for i in f.readlines():
    e=tuple(map(int,i.split()))
    edgelist.append(e)
    
    if e[0]>maxvertex:
        maxvertex=e[0]
    
#maxvertex=max(edgelist,key=itemgetter(1))[0]
#
orderingdict={}

def getchildren(ve,dire):
    children=[]
    if dire=='rev':
        for i in edgelist:
            if i[1]==ve and i[0] not in exploredinloop and i[0] not in explored:
                children.append(i[0])
    elif dire=='straight':
        for i in edgelist:
            if i[0]==ve and i[0] not in exploredinloop and i[0] not in explored:
                children.append(i[1])
    return children
        
        
    
explored=set()
def dfs(v):
    global t
    global exploredinloop
    global explored
    explored=set()
    children=getchildren(v,'rev')
    if len(children)==0:
        return
        
    for i in children:
        explored.add(i)
        dfs(i)
        orderingdict[t]=i
        t+=1
        exploredinloop.add(i)
        
t=1
exploredinloop=set()
def dfsloop(vertex):
    global t
    t=1
    global exploredinloop
    exploredinloop=set()
    for i in range(vertex,-1,-1):
        if i not in exploredinloop:
            dfs(i)
            
def dfs1(v):
    global exploredinloop
    global explored
    explored=set()
    children=getchildren(v,'straight')
    if len(children)==0:
        return
        
    for i in children:
        explored.add(i)
        dfs(i)
        exploredinloop.add(i)
    return len(explored)

def dfsloop1(vertex):
    global sccsizes
    global exploredinloop
    exploredinloop=set()
    for i in range(vertex,-1,-1):
        if orderingdict[i] not in exploredinloop:
            sccsizes.add(dfs1(i))

sccsizes=set()
dfsloop(maxvertex)
    
dfsloop1(maxvertex)

print(sccsizes)

