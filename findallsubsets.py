# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:41:35 2017

@author: vc185059
"""

def findallsubsets(l):
#    ln=len(l)
    if len(l)==0:
        return set(((),))
    else:
        aset=findallsubsets(l[1:])   
        aaset=aset.copy()
        for i in aaset:
            li=(l[0],)+i
            aset.add(li)
        
    return aset
    
    
a=findallsubsets((1,2,3,4))

print(a)