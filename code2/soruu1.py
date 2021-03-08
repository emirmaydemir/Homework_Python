# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:54:09 2020

@author: risin
"""

ogrenciler={"Emir":"102"}
while True:
    isim=input("isim giriniz: ")
    no=input("numara giriniz: ")
    ogrenciler[isim]=no
    devam=input("devam etmek isiyorsanız E istemiyorsanız H basınız: ")
    if(devam=="E"):
        pass
    else:
        break   
print(ogrenciler.items())
    
    

    
    