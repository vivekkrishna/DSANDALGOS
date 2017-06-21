# -*- coding: utf-8 -*-
"""
Created on Tue May  2 07:32:05 2017

@author: vc185059
"""

import random

def parsegraph(filename):

    f=open(filename,'r')
    
    vertices=[]
    edges=set([])
    
    for i in f.readlines():
        l=list(map(int,i.split()))
        vertex=l.pop(0)
        el=[tuple(sorted([vertex,j])) for j in l]
        
        vertices.append(vertex)
        edges.update(el)
        
    return vertices,list(edges)
    
    
def Randomcontraction(vertices,edges):
    
    while len(vertices)>2:
        (a,b)=random.choice(edges)
        vertices.remove(b)
        
        newedges=[]
        for e in edges:
            if e==(a,b):
                continue
            if b in e:
                if e[0]==b:
                    newedges.append(tuple(sorted([a,e[1]])))
                else:
                    newedges.append(tuple(sorted([a,e[0]])))
            else:
                newedges.append(e)
                
        edges=newedges
        
    return vertices,edges
    


    

vertices,edges=parsegraph('kargerMinCut.txt')
#random.seed(0)
mincutval=float('inf')
for i in range(1,1000):
    vertices,edges=Randomcontraction(vertices,edges)
    if len(edges)<mincutval:
        mincutval=len(edges)
    
print('min cut": %d' % mincutval)



