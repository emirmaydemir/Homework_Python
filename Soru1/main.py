liste=[]
while(True):
    str = input("Kelime giriniz: ")
    if str=='quit':# kullanıcı quit yazar ise giriş sonlanacak
        break
    elif str=='Quit':
        break
    else:
        liste.append(str)# quit girilmediği sürece dizimizin içine ekleme yapıyoruz
print(liste[::-1])
for i in liste[::-1]:#listemizi ters çevirip tersten yazdiriyoruz
    print(i)