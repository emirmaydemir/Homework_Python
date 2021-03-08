
def fonk(liste,max,liste3):
    if len(liste)==0:
        return liste3
    else:
        if max < liste[0]:
            liste3.append(max)
            return fonk(liste[1:],max,liste3)
        else:
            liste3.append(liste[0])
            return fonk(liste[1:],max,liste3)



boyut=0
b=0
liste3=[]
liste4=[]
isim=input("dosya ismi giriniz: ")
try:
    dosya=open(isim,"r")
except FileNotFoundError:
    print("dosya bulunamadi")
liste=dosya.read().split()
liste2=[]
for i in liste:
    liste2.append(int(i))
print("Dosyadaki elemanlar: ",liste2)
for i in liste:
    boyut=boyut+1
print("Dosyanin boyutu: ",boyut)
while True:
    max=input("Max değeri giriniz: ")
    if max.isdigit() or  max.lstrip("-").isdigit():
        max=int(max)
        break;
    else:
        print("Lütfen integer değer giriniz ")
son=fonk(liste2,max,liste3)
print(son)
for i in son:
    liste4.append(str(i))
dosya.close()
dosya=open(isim,"w")
dosya.seek(0)
for i in liste4:
    dosya.write(str(i))
    dosya.write(" ")
dosya.close()