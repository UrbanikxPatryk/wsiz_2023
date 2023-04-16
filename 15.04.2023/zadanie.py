# Zadanie A
s = ['aa', 'a', 'c', 'bb']
def SPR(s):



    w = set(s)

    if len(s)==len(w):
        return True
    else:
        return False



# zadnie B 
def SPR2(w):

    wyg=set()
    for x in  w:
        if w.count(x)>1:
            wyg.add(x)
        if len(wyg)==0:
            return False

        return True, wyg

print(SPR(s))
print(SPR2(s))