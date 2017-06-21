# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:36:55 2017

@author: vc185059
"""

# Mergesort

"""

Time complexity: O(nlogn)

There are total logn levels in the recursion tree.

number of operations at any particular level is 

At level j, there are 2^j nodes, len of sub problem at each node is O(n/(2^j))

i.e. at each level O(2^j)*O(n/(2^j)), cancelling 2^j , it is O(n)

For all levels in the order of O(nlogn)
"""
def Mergesort(L):
    
    if len(L)==1:
        return L
    
    mid=int(len(L)/2)
    l1=L[:mid]
    l2=L[mid:]
    
    sortedl1=Mergesort(l1)
    sortedl2=Mergesort(l2)
    
    outL=[]
    i=0
    j=0
    while i!=len(sortedl1) and j!=len(sortedl2):  
        if sortedl1[i]<=sortedl2[j]:
            outL.append(sortedl1[i])
            i+=1
        else:
            outL.append(sortedl2[j])
            j+=1
            
    if i==len(sortedl1):
        outL+=sortedl2[j:]
    else:
        outL+=sortedl1[i:]
#        
    return outL
    
def numofinversionsofMergesort(L):
    
    if len(L)==1:
        return (L,0)
    
    mid=int(len(L)/2)
    l1=L[:mid]
    l2=L[mid:]
    
    (sortedl1,inv1)=numofinversionsofMergesort(l1)
    (sortedl2,inv2)=numofinversionsofMergesort(l2)
    
# recursions are of equal size, so can make use of master method for calculating running time.    
    
    outL=[]
    
    inv3=0    
    
    i=0
    j=0
    while i!=len(sortedl1) and j!=len(sortedl2):  
        if sortedl1[i]<=sortedl2[j]:
            outL.append(sortedl1[i])
            i+=1
        else:
            outL.append(sortedl2[j])
            inv3+=len(sortedl1)-i
            j+=1
            
    if i==len(sortedl1):
        outL+=sortedl2[j:]
    else:
        outL+=sortedl1[i:]
#        
    return (outL,inv1+inv2+inv3)
    
    
""" Quick sort
   
Less additional space required, O(nlogn) on average   

Random pivots
   
"""

def quicksort(L):

    if len(L)==1:
        return (L,0)
    elif len(L)==0:
        return ([],0)
        
#    L[0],L[-1]=L[-1],L[0]
        
        
    # choose median of first mid and last element for pivot
    
    if len(L)%2==0:
        mid=int(len(L)/2)-1
    else:
        mid=int(len(L)/2)
    
    medianlist=[L[0],L[mid],L[-1]]
    aso=sorted(medianlist)
    
    inde=medianlist.index(aso[1])
    
    if inde==1:
        L[0],L[mid]=L[mid],L[0]
    elif inde==2:
        L[0],L[-1]=L[-1],L[0]
    
    pivot=L[0]
    
    i=1
    
    for j in range(1,len(L)):
        if L[j]<pivot:
            L[j],L[i]=L[i],L[j]
            i+=1
    
    L[i-1],L[0]=L[0],L[i-1]
    
    (l1,c1)=quicksort(L[:i-1])
    
    (l2,c2)=quicksort(L[i:])
    
    # return sorted list and number of comparisions
    return (l1+[pivot]+l2,len(L)-1+c1+c2)

#L=[5,4,6,2,1]
f=open('QuickSort.txt','r')
L=[]
for i in f:
    L.append(int(i))
    

sortlist=quicksort(L)
print(sortlist[1])