# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 18:30:32 2020

@author: risin
"""
print("Lütfen küçük harf kullanınız")
def yaz(kelime,boyut,keyNumber):
    string="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    for i in range(boyut):
        for j in range(26):
            if kelime[i]==string[j]:
                kelime[i]=string[j+keyNumber]
                break
    return kelime

def coz(kelime,boyut,keyNumber):
    string="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    for i in range(boyut):
        for j in range(26):
            if kelime[i]==string[j]:
                kelime[i]=string[j-keyNumber]
                break
    return kelime

liste1=[100]
string="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
secim='E'
while(secim=='E'):
    boyut=0
    keyNumber=int(input("anahtar sayıyı giriniz: "))
    kelime=input("kelimeyi giriniz: ")
    keyNumber=keyNumber%26
    kelime=list(kelime)
    secim2=input("Yazmak için Y çözmek için C basınız: ")
    for i in kelime:
        boyut=boyut+1
      
    if secim2=='Y':
        kelime=yaz(kelime,boyut,keyNumber)
        for i in kelime:
            print(i,end="")
    if secim2=='C':
        kelime=coz(kelime,boyut,keyNumber)
        for i in kelime:
            print(i,end="") 
    print("\n")
    secim=input("Devam etmek istiyorsanız E istemiyorsanız H basınız: ")
    
 







