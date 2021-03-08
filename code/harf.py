# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:22:44 2020

@author: risin
"""

for i in range(35):
    if i<10:
        print("A",end="")
        
    elif i>10 and i<18:
        print("B",end="")
        
    elif i>18 and i<27 and i%2==0:
        print("D",end="")
        
    elif i>18 and i<27 and i%2==1:
        print("C",end="")
        
    elif i>27 and i<34:
        print("F",end="")
        
    elif i==34:
        print("G",end="")