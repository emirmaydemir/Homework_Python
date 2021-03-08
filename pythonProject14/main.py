import itertools

import numpy as np

def polindrom(kelime):
    if kelime == kelime[::-1]:
        return kelime.replace(' ','')
a=0
chars = "abcdefghijklmnopqrstuvwxyz"
str=input("Kelime giriniz (lütfen boşluklu ifade girmeyiniz ve lütfen harfleri küçük giriniz): ")
kontrol = str
sozluk = {}
for s in kontrol:
  if s in sozluk:
    sozluk[s] += 1
  else:
    sozluk[s] = 1
for key in sozluk:
  if sozluk[key] > 1:
    print (key, "=",sozluk[key],"adet")
ihtimaller=[]
for i in range(5,len(str)+1):
    for permutasyon in itertools.permutations(str, i):
        strr = "".join(permutasyon)
        kelime=polindrom(strr)
        if not kelime in ihtimaller:
            ihtimaller.append(kelime)
for i in ihtimaller:
    print(i)
    a=a+1
print(a-1,"ihtimal bulundu")






