# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 15:40:55 2017

@author: vc185059
"""

# another approach is use a dict/list to track the top element of each stack
# to reduce time complexity to O(1) rather than traversing through the stack for 
# for top element

l=[[None,float('inf')] for _ in range(12)]

topstack=[0,0,0]

minsinstack=[float('inf') for _ in range(3)]

def push(value,stacknum):
    
    global l
    global topstack
    listlen=int(len(l)/3)
    
    start=listlen*(stacknum-1)
    
    index=start+topstack[stacknum-1]
    
    l[index][0]=value
    l[index][1]=minsinstack[stacknum-1]
    
    if minsinstack[stacknum-1]>value:
        minsinstack[stacknum-1]=value
    
    topstack[stacknum-1]+=1
#    for i in range(listlen):
#        if l[i+start]==None:
#            l[i+start]=value
#            break

def pop(stacknum):
    
    global l
    global topstack
    listlen=int(len(l)/3)
    
    start=listlen*(stacknum-1)
    
    returnval=l[start+topstack[stacknum-1]-1][0]
    
    l[start+topstack[stacknum-1]-1][0]=None
    
    minsinstack[stacknum-1]=  l[start+topstack[stacknum-1]-1][1]  
    
    topstack[stacknum-1]-=1    
    
    return returnval
#    for i in range(listlen):
#        if l[i+start]==None:
#            if i==0:
#                return None
#            else:
#                tmp=l[i+start-1]
#                l[i+start-1]=None
#                return tmp
    
def mini(stacknum):
    
    return minsinstack[stacknum-1]        
    
push(1,1)