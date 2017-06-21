# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:21:32 2017

@author: vc185059
"""
#aset=set()
#for i in range(0,5):
#    
#    for j in range(i+1):
#        for k in range(i+1):
#            
#            if (j,k) not in aset:
#                print(j,k,end='   ')
#            aset.add((j,k))
#            
#    print()

def findislandlen(i,j,count):
    global visitedones
    visitedones.add((i,j))
    count+=1
    neighborlist=findoneneighbors(i,j)
    for each in neighborlist:
        if each not in visitedones:
            count=findislandlen(each[0],each[1],count)
    return count
    
def findoneneighbors(i,j):
    
    neighbors=[]
    for k in range(i-1,i+2):
        for l in range(j-1,j+2):
            try:
                if k>=0 and l>=0 and arr[k][l]==1:
                    neighbors.append((k,l))
            except:
                continue
    return neighbors
        
arr=[[0,0,1,1,0],
     [1,0,1,1,0],
     [0,1,0,0,0], 
     [0,0,0,0,1]]
     
hei=len(arr)
wid=len(arr[0])
counts=[]
visitedones=set()
for i in range(hei):
    for j in range(wid):
        if arr[i][j]==1 and (i,j) not in visitedones:
            count=findislandlen(i,j,0)
            counts.append(count)
            
print(max(counts))
