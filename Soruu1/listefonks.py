def topla(liste):
    toplam=0
    for i in liste:
        toplam=toplam+i
    return toplam
def carp(liste):
    carpim=1
    for i in liste:
        carpim=carpim*i
    return carpim
def max(liste):
    max=0
    for i in liste:
        if max<i:
            max=i
    return max
def min(liste):
    min=1000000
    for i in liste:
        if min>i:
            min=i
    return min
def ort(liste):
    toplamm=0
    boyut=0
    for i in liste:
        toplamm=toplamm+i
        boyut=boyut+1
    return toplamm/boyut
def arama(liste,aranan):
    kontrol=False
    for i in liste:
        if i==aranan:
            kontrol=True
    return kontrol
def siralama(liste,boyut):
    for i in range(0,boyut-1):
        for j in range(i+1,boyut):
            if liste[i]>liste[j]:
                temp=liste[j]
                liste[j]=liste[i]
                liste[i]=temp
    return liste
def essiz(liste,boyut):
    a=boyut-1
    b=0
    liste2=liste
    for i in range(0,boyut-1):
        for j in range(i+1,boyut):
            if liste[i]==liste2[j]:
                liste2[j]=0
    while(a!=-1):
        if liste2[a]==0:
            liste2.pop(a)
        a=a-1
    return liste2
