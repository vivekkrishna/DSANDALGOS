# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:57:45 2017

Finding if there is a loop and starting point of loop.

@author: vc185059
"""

class node():
    def __init__(self,value):
        self.value=value
        self.next=None
        



def createalinkedlist(startnode):
    wanttoaddnode='1'
    currentnode=startnode
    i=0
    #mergenode=None
    while wanttoaddnode=='1':
        wanttoaddnode=input('enter 1 if you want to add another node, else 0')
        if wanttoaddnode=='1':
            i+=1
            nodevalue=input('enter next node value')
            nextnode=node(nodevalue)
#            if i==4:
#                mergenode=nextnode
            currentnode.next=nextnode
            currentnode=nextnode
        else:
            #currentnode.next=mergenode
            break
        
def printlinkedlist(startnode):
    currentnode=startnode
    print(currentnode.value,end=' ')
    while currentnode.next!=None:
        currentnode=currentnode.next
        print(currentnode.value,end=' ')
        
        
def loopnode(startnode):
    
    loopexists=False
    slownode=startnode
    fastnode=startnode.next
    
    while slownode!=fastnode and slownode!=None and fastnode!=None and fastnode.next!=None:
        slownode=slownode.next
        fastnode=fastnode.next.next
    
    if slownode==None or fastnode==None:
        loopexists=False
        return None
    else:
        loopexists=True
        loopnode=fastnode
    
    if loopexists:
        slownode=startnode
        
        while 1:
            
            if loopnode==slownode:
                return slownode
        
            fastnode=loopnode.next
            
            while fastnode!=loopnode:
                if fastnode==slownode:
                    return slownode
                fastnode=fastnode.next
            slownode=slownode.next
            
            
def MergetwosortedLLs(stnode1,stnode2):
    prevnode=None
    while stnode1!=None and stnode2!=None:
        stnode3=getnextbest(stnode1,stnode2)
        if prevnode!=None:
            prevnode.next=stnode3
        if stnode3==stnode1:
            stnode1=stnode1.next
        else:
            stnode2=stnode2.next
        prevnode=stnode3
    if stnode1==None:
        prevnode.next=stnode2
    else:
        prevnode.next=stnode1
        
def getnextbest(node1,node2):
    if int(node1.value)<=int(node2.value):
        return node1
    else:
        return node2