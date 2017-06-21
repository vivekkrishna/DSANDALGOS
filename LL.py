# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:17:25 2017

@author: vc185059
"""

class node():
    def __init__(self,value):
        self.value=value
        self.next=None
        



def createalinkedlist(startnode):
    wanttoaddnode='1'
    currentnode=startnode
    while wanttoaddnode=='1':
        wanttoaddnode=input('enter 1 if you want to add another node, else 0')
        if wanttoaddnode=='1':
            nodevalue=input('enter next node value')
            nextnode=node(nodevalue)
            currentnode.next=nextnode
            currentnode=nextnode
        else:
            break
        
def printlinkedlist(startnode):
    currentnode=startnode
    print(currentnode.value,end=' ')
    while currentnode.next!=None:
        currentnode=currentnode.next
        print(currentnode.value,end=' ')
        
def swapadj(startnode):
    currentnode=startnode
    nextnode=startnode.next
    startnode=nextnode
    prevnode=None
    while currentnode!=None and nextnode!=None:
        try:
            temp=nextnode.next
        except:
            temp=None
        nextnode.next=currentnode
        if prevnode!=None:
            prevnode.next=nextnode
        prevnode=currentnode
        currentnode=temp
        try:
            nextnode=temp.next
        except:
            nextnode=None
    prevnode.next=currentnode
    return startnode

startnode=node(5)
createalinkedlist(startnode)
printlinkedlist(startnode)
print()
startnod=swapadj(startnode)
print()
printlinkedlist(startnod)