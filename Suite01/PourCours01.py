import os
print ("a")
os.chdir("C:/Users/gaetan.ickx/Documents/python/cours 2018")
currentD=os.getcwd()
print(currentD)
monficher=open("fichier.txt", "r")
contenu=monficher.read()
textAajouter="bonjour ceci est un test d'écriture3232"
print(contenu)
monficher.close()
print(monficher)
monficher =open("fichier.txt", "w")
monficher.write(textAajouter)
monficher.close
monficher=open("fichier.txt", "r")
contenu=monficher.read()
print(contenu)
import pickle
score={
    "J1":5,
    "J2":7
}
with open ('data01', 'wb') as Fichier:
    depickler01=pickle.Pickler(Fichier)
    depickler01.dump(score)

with open ('data01', 'rb') as Fichier:
    depickler01=pickle.Unpickler(Fichier)
    scoreRecup=depickler01.load()
print (scoreRecup)

a = 1