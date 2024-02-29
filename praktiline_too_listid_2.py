print("\n#7: Sorteerimine\n")
#7: Sorteerimine Teil on vaja luua programm, mis sorteerib numbrite nimekirja kahaneva/kasvava absoluutväärtuse järgi.
chisla=[]
mitu=int(input("Mitu arvu sa tahad kirjutada? "))
for i in range(mitu):
    a=abs(int(input("Sisetage oma arvud ")))
    chisla.append(a)
   

chisla.sort()       #sorteerimine
print("Kasvava loeng on:",chisla)
chisla.sort(reverse=True)  #указывает на то, что сортировка должна быть выполнена в порядке убывания
print("Kahaneva loeng on:",chisla)

print("\n#9: Nimi kontroll\n")

#9: Nimi kontroll
v=k=0
vokaali=["a","e","y","u","i","o","a"]
konsonanti="qwrtpsdfghjklzxcvbnm"         

nimi=input("Kirjuta siia oma nimi: ")


if nimi.isalpha():
    print("Tere,",nimi.capitalize(),"!")
    mitu=len(nimi)
    print("Teie nimil on",mitu,"tähed.")
    nimi=nimi.lower()
    tahed=list(nimi)
    for sümbol in tahed:
        if sümbol in vokaali:
            v+=1
        elif sümbol in konsonanti:
            k+=1
            k+=1
    print("Vokaali:",v)
    print("Konsonanti:",k)
    nimi=sorted(set(nimi))    #уникальные элементы в множестве
    print(f"Sorteeritud tähed:",nimi)
else:
    print("Siin ei pea olema numbrid")
    

print("\n#12 Koostage loend 10 juhuslikust numbrist 1 kuni 100\n")

#12 Koostage loend 10 juhuslikust numbrist 1 kuni 100. Kirjutage programm, mis vahetab selle loendi miinimaalse ja maksimaalse elemendid
from random import *
spisok=[]
for i in range(10):
    spisok.append(randint(1,100))

print("Juhuslik loend on:",spisok)

minimum=spisok.index(min(spisok))
maximum=spisok.index(max(spisok))

spisok[minimum],spisok[maximum] = spisok[maximum],spisok[minimum]  #обмен местами у элементов списка

print("Uus loend:",spisok)

print("\n11\n")
#11

n=int(input("Sisestage tähtede arv (n): "))
tahestik="abcdefghijklmnopqrstuvwxyz"
tahed_loend=[]

for i in range(n):
    taht=tahestik[i]
    palju_tahed=taht*(i+1)
    tahed_loend.append(palju_tahed)

print(tahed_loend)

print("\n16\n")
#16

import random

kusimus=input("Tere! Esitage oma küsimus(jah/ei): ")
vastused=["Jah, muidugi!","Jah!","Võib-olla!","Ei!"]
indeks = random.randint(0, len(vastused) - 1)
vastus = vastused[indeks]
print("vastus teie küsimusele","(",kusimus,")","on:",vastus)
