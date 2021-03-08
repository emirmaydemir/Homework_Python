islem=input("bir işlem giriniz: ")
sag=0
sol=0
for i in islem:
    if i=="(":
        sol=sol+1
    elif i==")":
        sag=sag+1
    else:
        pass

if sag>sol:
    print(str(sag-sol)+" adet ')' fazla")
elif sol>sag:
    print(str(sol-sag) + " adet '(' fazla")
else:
    print("parantez hatası yoktur")