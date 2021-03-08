# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:52:14 2020

@author: risin
"""
a=0
b=0
list=[]
j=0
toplam=0
sayi=input("sayi giriniz")
tersi=sayi[::-1]
print(tersi)
for i in sayi:
    a=a+1

print(a)


for i in range(a):
    if sayi[i]==tersi[i]:
        b=b+1
        
if a==b:
    print("sayi palindrom")