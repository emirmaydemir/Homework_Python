import listefonks
aranan=int(input("aranan sayiyi gir: "))
liste=[1,2,1,2,3,4,5]
boyut =0
for i in liste:
    boyut=boyut+1
kontrol=listefonks.arama(liste,aranan)
if kontrol==True:
    print("Aranan rakam bulundu")
else:
    print("Aranan rakam bulunamadı")
toplam=listefonks.topla(liste)
print("Listedeki elemanların toplamı ",toplam)
carpim=listefonks.carp(liste)
print("Listedeki elemanların çarpımı ",carpim)
max=listefonks.max(liste)
print("Listedeki en büyük eleman ",max)
min=listefonks.min(liste)
print("Listedeki en küçük eleman ",min)
ort=listefonks.ort(liste)
print("Listedeki elemanların ortalaması ",ort)
sirali=listefonks.siralama(liste,boyut)
print("Listedeki elemanların siralamasi ",sirali)
listee=listefonks.essiz(liste,boyut)
print("Listenin eşsiz hali ",listee)






