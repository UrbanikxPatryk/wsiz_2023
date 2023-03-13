import asyncore
import os
import random 

def Spawdznie(a,b):
   
    wynik=[]
    for x in a :
        
     for y in b:
        if y%x==0:
            wynik.append(x)
    os.system("cls")        
    print(f"Liczby podzielne{wynik}")       



def Generator():
    a =[]
   
    for w in range(4):
        W=random.randint(1,100)
        a.append(W)
    print(f"wylosowane liczby A={a}")
  
   
  
     
      
      



Spawdznie(a=[2,5,7,9],b=[4,8,18,27])

Generator()