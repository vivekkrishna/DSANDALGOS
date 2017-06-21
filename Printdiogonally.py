# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:16:03 2017

@author: vc185059
"""


def printdiagonally(l):
    nextdir='down'
    currindex=[0,0]
    print(l[currindex[0]][currindex[1]])   
    currindex[1]+=1
    while currindex[0]!=len(l)-1:
        print(l[currindex[0]][currindex[1]])
        if currindex[1]==0 or currindex[1]==len(l[0])-1:
            nextdir='stdown'
        if nextdir=='up':
            currindex[0]-=1
            currindex[1]+=1
        elif nextdir=='down':
            currindex[0]+=1
            currindex[1]-=1
        elif nextdir=='stdown':
            currindex[0]+=1
            print(l[currindex[0]][currindex[1]])
            if currindex[1]==0:
                currindex[0]-=1
                currindex[1]+=1
                nextdir='up'
            elif currindex[1]==len(l[0])-1:
                currindex[0]+=1
                currindex[1]-=1
                nextdir='down'
    
    while currindex[1]!=len(l[0]):
        print(l[currindex[0]][currindex[1]])   
        currindex[1]+=1
        
        
l=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]
   
printdiagonally(l)

        
    