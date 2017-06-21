# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:40:49 2017

@author: vc185059
"""

def locsfornextqueen(locsofprevqs):
    locs=[]
    for i in 'ABCDEFGH':
        for k in locsofprevqs:
            if i in k:
                break
        else:
            for j in range(1,9):
                if consistent(i+str(j),locsofprevqs):
                    locs.append(i+str(j))
            break
    return locs
    
def consistent(loc,locsofprevqs):
    for i in locsofprevqs:
        alpha='ABCDEFGH'
        diff1=abs(alpha.index(loc[0])-alpha.index(i[0]))
        diff2=abs(int(loc[1])-int(i[1]))
        if loc[0] in i or loc[1] in i or (diff1==diff2):
            return False
    return True
    
def findallcombs(comb,combs):
    if len(comb)==8:
        combs.append(comb)
        
    locs=locsfornextqueen(comb)
    for i in locs:
        findallcombs(comb+[i],combs)
        
    return combs
        
finalcombs=findallcombs([],[])
print(len(finalcombs))