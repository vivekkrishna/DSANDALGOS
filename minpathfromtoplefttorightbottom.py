# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 15:23:14 2017

@author: vc185059
"""
pathdict={}

def minpathfromtoplefttorightbottom(l,i,j):
    
    global pathdict
    
    if i==len(l)-1 and j==len(l[0])-1:
        return [l[i][j]]
        
    takep1=False
    takep2=False
    
    if i!=len(l)-1:
        try:
            p1=pathdict[(i+1,j)]
        except KeyError:
            p1=minpathfromtoplefttorightbottom(l,i+1,j)
    else:
        takep2=True
        
    if j!=len(l[0])-1:
        try:
            p2=pathdict[(i,j+1)]
        except KeyError:
            p2=minpathfromtoplefttorightbottom(l,i,j+1)
    else:
        takep1=True
        
    if takep1:
        return [l[i][j]]+p1
        
    if takep2:
        return [l[i][j]]+p2
    
    if (i+1,j) not in pathdict:
        pathdict[(i+1,j)]=p1
    if (i,j+1) not in pathdict:
        pathdict[(i,j+1)]=p2
    
    if sum(p1)<sum(p2):
        return [l[i][j]]+p1
    else:
        return [l[i][j]]+p2
    
l=[[1,7,9,2],[8,6,3,2],[1,6,7,8],[2,9,8,2]]
finalpath=minpathfromtoplefttorightbottom(l,0,0)