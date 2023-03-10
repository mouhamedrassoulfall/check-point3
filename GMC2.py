#exercice1
def listMultiply(liste):
    r = 1
    for x in liste:
        r *= x
    return r

l = [2, 3, 6]
print(listMultiply(l))

#exercice2
def getkey(l):  #fonction permetant de choisir l'element à trier
    return l[1]

t = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(t, key=getkey))

#exercice3
d1 = { 'a' : 100, 'b' : 200, 'c' : 300}

d2 = {'a' : 300, 'b' : 200, 'd' : 400}


for key in d1:
    if key in d2 :
        d1[key] = d1[key] + d2[key] #addition des element qui ont les mêmes mots clé
    else:
        pass
    
print(d1)




#exercice4
n= int(input("entrer un nombre")) #demander un nombre a l'utilisateur

d={} #initialiser le dictionaire
for i in range(1,n+1): 
    d[i]=i*i # donner la valeur carre de i a tout les clés i
print(d)



#exercice4
def getkey(liste):  #fonction permetant de choisir l'element à trier
    return liste[1]

liste = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
sorted = sorted(liste, key=getkey , reverse= True) # trie de maniére décroissant
print(sorted)



#exercice6
ensemble= {0, 1, 2, 3, 4}
for x in ensemble:
    print(x)
ensemble.add(12)
ensemble.remove(3)