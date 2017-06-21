# -*- coding: utf-8 -*-
"""
Created on Wed May  3 07:41:00 2017

@author: vc185059
"""

from operator import itemgetter

f=open('SCC.txt','r')
#edgelist=[]
dictedges={}
maxvertex=0
for i in f.readlines():
    e=tuple(map(int,i.split()))
    if e[0]==e[1]:
        continue
    #edgelist.append(e)
    try:
        dictedges[e[0]][0]+=[e[1]]
    except KeyError:
        dictedges[e[0]]=[[e[1]],[]]
        
    try:
        dictedges[e[1]][1]+=[e[0]]
    except KeyError:
        dictedges[e[1]]=[[],[e[0]]]
        
    
    if e[0]>maxvertex:
        maxvertex=e[0]
    
#maxvertex=max(edgelist,key=itemgetter(1))[0]
#


def getchildren(ve,dire):
    children=[]
    if dire=='rev':
        try:
            for i in dictedges[ve][1]:
                if i not in exploredinloop and i not in explored:
                    children.append(i)
        except KeyError:
            pass
    elif dire=='straight':
        try:
            for i in dictedges[ve][0]:
                if i not in exploredinloop and i not in explored:
                    children.append(i)
        except KeyError:
            pass
    return children
        
        
ordering=[]
  
explored=set()
def dfs(v):
    global exploredinloop
    global explored
    global ordering
    explored=set()
    frontier_set=[v]
    while len(frontier_set)>0:
        val=frontier_set[-1]
        children=getchildren(val,'rev')
        explored.add(val)
        if len(children)==0:
            ordering.append(val)
            exploredinloop.add(val)
            del frontier_set[-1]
        else:
            frontier_set+=children
            explored.update(children)
    
#def dfs(v):
#    global t
#    global exploredinloop
#    global explored
#    explored=set()
#    children=getchildren(v,'rev')
#    if len(children)==0:
#        return
#        
#    for i in children:
#        explored.add(i)
#        dfs(i)
#        orderingdict[t]=i
#        t+=1
#        exploredinloop.add(i)
        
exploredinloop=set()
def dfsloop(vertex):
    global exploredinloop
    exploredinloop=set()
    for i in range(vertex,-1,-1):
        if i not in exploredinloop:
            dfs(i)
            
def dfs1(v):
    global exploredinloop
    global explored
    explored=set()
    frontier_set=[v]
    while len(frontier_set)>0:
        val=frontier_set[-1]
        children=getchildren(val,'straight')
        explored.add(val)
        if len(children)==0:
            exploredinloop.add(val)
            del frontier_set[-1]
        else:
            frontier_set+=children
            explored.update(children)
    return len(explored)
            
#def dfs1(v):
#    global exploredinloop
#    global explored
#    explored=set()
#    children=getchildren(v,'straight')
#    if len(children)==0:
#        return
#        
#    for i in children:
#        explored.add(i)
#        dfs(i)
#        exploredinloop.add(i)
#    return len(explored)

def dfsloop1(vertex):
    global sccsizes
    global exploredinloop
    exploredinloop=set()
    for i in range(vertex,-1,-1):
        if ordering[i] not in exploredinloop:
            sccsizes.append(dfs1(ordering[i]))

sccsizes=[]
dfsloop(maxvertex)
    
dfsloop1(maxvertex)

print(sccsizes)

