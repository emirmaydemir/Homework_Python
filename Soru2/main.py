
liste=[]#kullanıcının girdiği elemanları tutacak
liste2=[]#en küçük 2. elemanı tekrar sayısı kadar tutacak
while(True):
    sayi = input("Tam sayi giriniz: ")
    if sayi=='quit':#quit yazdığımızda çıkış yapacak
        break
    elif sayi=='Quit':
        break
    elif sayi=='':#kullanıcı yanlışıkla enter basarsa işleme devam edicek
        continue
    else:
        liste.append(int(sayi))#girilen string sayı degerini integere çevirdik ve listemize ekledik
max=0
for i in liste:
    if i>max:#max değeri bulma sebebimiz min değerlerin içerisine atayacağız ilk if bloğunda sorun oluşmaması amaçlı
        max=i
min=max
min2=max+1
for i in liste:
    if(i<min):
        min2=min     ## bu for döngüsünde listeden gelen i değerinin en küçük değer olması en küçük değerden büyük
        min=i         ## olması veya en küçük değere eşit olması durumlarını inceledik
    elif(i<min2 and i!=min):
        min2=i
    else:
        if min2 == min:
            min2 = i
for i in liste:
    if(min2==i):
        liste2.append(i)##ikinci en büyük değerimizin tekrar sayısı kadar listenin içerisine eklenme işlemi
print(liste2)##ekrana bastırdık