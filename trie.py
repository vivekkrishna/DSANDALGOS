# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 10:29:27 2017

trie implementation

@author: vc185059
"""

class node():
    def __init__(self,value):
        self.value=value
        self.children=[]
    def addchild(self,anode):
        self.children.append(anode)
        


        
        
        
        
startnode=node('0')

def addwordintrie(snode,stri):
    valuefound=False
    if stri=='':
        return
    for i in snode.children:
        if i.value==stri[0]:
            valuefound=True
            addwordintrie(i,stri[1:])
    if valuefound==False:
        childnode=node(stri[0])
        snode.children.append(childnode)
        addwordintrie(childnode,stri[1:])
        
def getwordswithprefix(snode,stri,words,word):
    
    if stri!='':
        valuefound=False
        for i in snode.children:
            if i.value==stri[0]:
                valuefound=True
                word+=i.value
                getwordswithprefix(i,stri[1:],words,word)
        if valuefound==False:
            return
    else:
        if len(snode.children)==0:
            words.append(word)
            return
        else:
            for i in snode.children:
                word2=word
                word2+=i.value
                getwordswithprefix(i,stri,words,word2)
                    
    return words
    
def dicttrie(snode,dictin,d):
    if len(snode.children)==0:
        return dictin
    else:
        for i in snode.children:
            try:
                dictin[d]+=[i.value]
            except KeyError:
                dictin[d]=[i.value]
            dicttrie(i,dictin,d+1)
            #print(i.value,end=' ')
        return dictin
            
dicti=dicttrie(startnode,{},1)
for i in dicti:
    print(dicti[i],end='\n')
    
            