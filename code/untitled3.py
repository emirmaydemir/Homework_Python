# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 18:31:01 2020

@author: risin
"""

sayi=input("sayi giriniz")
toplam=0
carpim=0

for i in sayi:
    toplam=toplam+int(i)
    if toplam<10:
        print("toplamsal kökü",toplam)
        break
    
for i in sayi:
    carpim=carpim*int(i)
    if carpim<10:
        print("carpimsal kökü",carpim)
        break