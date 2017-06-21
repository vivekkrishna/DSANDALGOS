# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 21:06:34 2017

@author: vc185059
"""

from operator import itemgetter
def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    rem_size=max_size
    finallist=[]
    
    if songs[0][2]<rem_size:
        finallist.append(songs[0][0])
        
    rem_size-=songs[0][2]
    
    del songs[0]
    
    songs=sorted(songs,key=itemgetter(2))
    
    for i in songs:
        
        if i[2]>rem_size:
            break
        else:
            finallist.append(i[0])
            rem_size-=i[2]
        
    print(finallist)
    
    
songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size=11   
song_playlist(songs,max_size)