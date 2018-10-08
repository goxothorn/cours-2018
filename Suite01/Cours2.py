import os
os.chdir("C:/Users/gaetan.ickx/Documents/python/cours 2018")
class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom=prenom
        self.age=33
        self.lieuResidence="BXL"

class Compteur:
    obj_cree=0
    def __init__(self):
        Compteur.obj_cree+=1

class TableauNoir:

    def __init__(self):
        self.surface=""
    def ecrire(self, message_a_ecrire):

        if self.surface!="":
            self.surface+="\n"
        self.surface+= message_a_ecrire

    def lire (self):
        print (self.surface)

    def effacer (self):
        self.surface=""

Nom= input("quel est votre nom")

class Zdict:
    def __init__(self):
        self._dictionnaire={}

    def __getitem__(self, index):
        return self._dictionnaire[index]

    def __setitem__(self, index, valeur):
        self._dictionnaire[index]= valeur

test1=Zdict


class Zdict2:
    def __init__(self):
        self.dictionnaire={}

    def __getitem__(self, index):
        return self.dictionnaire[index]

    def __setitem__(self, index, valeur):
        self.dictionnaire[index]= valeur


b=1
while b<5:
    test20[b]="{}er element".format(b)
    b+=1
b=1
while b<5:
    test20[b]
    b+=1

class Testin:
    def __init__(self):
        self.liste= []

    def __contains__(self, existe):
        for element in self.liste:
            if element==existe:
                print("Vrai")

    def affichage (self):
        print(self.liste)

a=2
if a == 1:
    print ("oui")
else: print("non")

test100 = Testin()
test100.__contains__(0)
test100.liste=[1,2,3,4,5]
test100.affichage()

for element in liste5:
    if element == 5:
        print("Vrai")
    else:
        print("Faux")