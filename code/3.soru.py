# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:31:59 2020

@author: risin
"""
import random
list=[]
toplam=0
max=0
max2=0
min2=0
cift=0



for i in range(20):
    sayi=random.randint(1,100)
    list.append(sayi)

print("dizi elemanlari: ",list)
min=list[0]

for i in range(0,20):
    toplam=toplam+list[i]
    
print("dizilerin ort: ",toplam/20)

for i in range (0,20):
    if max<list[i]:
        max=list[i]
        
for i in range (0,20):
    if min>list[i]:
        min=list[i]
        
for i in range(0,20):
    if list[i]%2==0:
        cift=cift+1
        
print("en kucuk ",min,"en buyuk ", max)
list.remove(max)
list.remove(min)
for i in range (18):
    if max2<list[i]:
        max2=list[i]

min2=list[4]
for i in range (18):
    if min2>list[i]:
        min2=list[i]

print("2. en büyük ",max2," 2. en kucuk ",min2)
print("dizideki çift sayisi",cift)
        