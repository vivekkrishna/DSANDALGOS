# -*- coding: utf-8 -*-
"""
Created on Thu May 11 08:49:09 2017

@author: vc185059
"""
import heapq

maxofminsheap=[]
minofmaxsheap=[]

medians=[]
f=open('median.txt','r')
l=[]
for i in f.readlines():
    l.append(int(i))
    if len(maxofminsheap)==0:
        heapq.heappush(maxofminsheap,-int(i))
        medians.append(int(i))
        continue
    elif len(minofmaxsheap)==0:
        if int(i)<-maxofminsheap[0]:
            heapq.heappush(minofmaxsheap,-heapq.heappop(maxofminsheap))
            heapq.heappush(maxofminsheap,-int(i))
        else:
            heapq.heappush(minofmaxsheap,int(i))
        medians.append(-maxofminsheap[0])
        continue
    if len(maxofminsheap)<=len(minofmaxsheap):
        if int(i)<=minofmaxsheap[0]:
            heapq.heappush(maxofminsheap,-int(i))
        else:
            heapq.heappush(maxofminsheap,-heapq.heappop(minofmaxsheap))
            heapq.heappush(minofmaxsheap,int(i))
    elif len(maxofminsheap)>len(minofmaxsheap):
        if int(i)>=-maxofminsheap[0]:
            heapq.heappush(minofmaxsheap,int(i))
        else:
            heapq.heappush(minofmaxsheap,-heapq.heappop(maxofminsheap))
            heapq.heappush(maxofminsheap,-int(i))
        
            
    if len(maxofminsheap)<len(minofmaxsheap):
        medians.append(minofmaxsheap[0])
    else:
        medians.append(-maxofminsheap[0])
        
print(len(minofmaxsheap))
print(len(maxofminsheap))
        
print(sum(medians))
    


#li=[4,6,2,0,3,2,1,6,8,7]
#
#heapl=[]
##heapq._heapify_max(li)
#for i in li:
#    
#    heapq.heappush(heapl,-i)
#    
#while len(heapl)!=0:
#    #print(heapl)
#    print(-heapq.heappop(heapl))