# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 17:56:32 2017

@author: vc185059
"""

grid=[[0,0,1,0],
      [0,1,1,0],
      [0,0,0,1],
      [0,0,0,0]]
      
def getneighbors(loc):
    i=loc[0]
    j=loc[1]
    neighbors=[]
    global grid
    for ii in range(max(i-1,0),i+2):
        for jj in range(max(j-1,0),j+2):
            if ii in range(4) and jj in range(4):
                if grid[ii][jj]!=1:
                    neighbors.append((ii,jj))
    return neighbors
                

def findallpaths(path,paths):
    
    if (3,3) in path:
        paths.append(path)
        return
    neighbors=getneighbors(path[-1])
    
    for i in neighbors:
        if i not in path:
            findallpaths(path+[i],paths)
    
    return paths
    
    
paths=findallpaths([(0,0)],[])