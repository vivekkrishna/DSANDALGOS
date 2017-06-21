# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:12:01 2017

@author: vc185059
"""

sumvalue=None

def findallpaths(p,k,paths):
    global sumvalue
    if sumvalue==None:
        sumvalue=k
    if k<0:
        return False
    else:
        if sum(p)==sumvalue:
            paths.append(p)
    findallpaths(p+[1],k-1,paths)
    findallpaths(p+[2],k-2,paths)
    findallpaths(p+[3],k-3,paths)
    return paths
    
print(findallpaths([],6,[]))