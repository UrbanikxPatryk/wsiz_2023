
import os


dane = [
     5, 0.7,
     10, 0.75,
     100, 2.4,
     200, 4.9,
     400, 11,
     800, 29,
     1600, 86,
     3200, 224,
     6400, 497,
     12800, 1092]

x,y = [],[] 

for wynik in dane:
     if dane.index(wynik) % 2 == 0 :
         os.system("cls")
         x.append(wynik)     
     else:
         os.system("cls")
         y.append(wynik)

print(f"x={x}\ny={y}")

# Zadanie =============================================================
a= [2,5,7,9] 
b=[4,8,18,27]

