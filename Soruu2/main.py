import Kontrol

kelime=input("Bir kelime giriniz: ")
aranan=input("aranan karakteri gir: ")
kontrol=Kontrol.kontrol(kelime,aranan)
if kontrol:
    print("aranan harf kelimede bulunuyor")
else:
    print("aranan harf kelimede bulunmuyor")