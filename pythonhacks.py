# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 21:25:36 2017

@author: vc185059
"""

#sort the list by an element in tuple

from operator import itemgetter
data = [('abc', 121),('abc', 231),('abc', 148), ('abc',221)]
sorted(data,key=itemgetter(1))
[('abc', 121), ('abc', 148), ('abc', 221), ('abc', 231)]


