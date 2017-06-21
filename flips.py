# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 20:19:46 2017

@author: vc185059
"""

li=[1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]

dicti={} #index tuple and count

def getvalue(i,remainingflips):
    count=0
    tup=()
    for i in range(i,len(li)):
        if li[i]==1:
            count+=1
        elif li[i]==0 and remainingflips!=0:
            count+=1
            remainingflips-=1
            tup+=(i,)
        else:
            break
    return (tup,count)
    
    
for i in range(len(li)):
    if li[i-1]==0 and li[i]==1:
        (tup,count)=getvalue(i,2)
        dicti[tup]=count
        
a=max(dicti,key=dicti.get)
print(a)      



