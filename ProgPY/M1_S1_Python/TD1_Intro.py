# Section 1 : Imports de module
import random
import math
from datetime import datetime
# Section 2 : Définition de fonctions

def palindrome(mot:str):
    mot_inv = ""
    for i in range(len(mot)):
        mot_inv += mot[-(i+1)] 
    return mot == mot_inv

def afficher_nb_jour(num_mois, num_annee):
    nb_jour_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    nb_jour_mois_bis = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    if (num_annee % 4 == 0 and not(num_annee % 100 == 0)) or (num_annee % 400 == 0):
        nb_jour =  nb_jour_mois_bis[num_mois-1]
    else:
        nb_jour = nb_jour_mois[num_mois-1]

    print(nb_jour)


def affiche_nom(nom:str="BOB", nombre:int=3):
    print(nom * nombre)

def calcul_age(jour, mois, annee):
    return (datetime.now().year - datetime(annee, mois, jour).year)


# Section 3 : Tests de fonctions définies et manipulations en mode "script"

# 2 - Types et fonctions de base
'3' * 10
3 * 10
# '3' * 10.0 # 10.0 est un float et l'on ne peut pas multiplier une chaine de caractère avec un flottant.
'3' + '3'
3 + 3
# '3' + 3 # On ne peut pas additionner une chaine de caractère avec un entier

mot = "kayak"
mot_inv = ""
for i in range(len(mot)):
    mot_inv += mot[-(i+1)] 
    #print(mot_inv)

print(mot == mot_inv)

print(palindrome("ressasser")) # Fonctionne dans ce cas.
print(palindrome("remasser")) # Ne fonctionne pas dans ce cas.

afficher_nb_jour(2, 2020) # Bissextile
afficher_nb_jour(2, 2021) # Non bissextile

affiche_nom()

# 3 - Focus sur les chaînes de caractères
replique_1_2 = "Je ne vous jette pas la pierre, Pierre,"
replique_2_2 = "mais j'étais à deux doigts de m'agacer"
chaine = replique_1_2 + " " + replique_2_2

print(len(chaine))

chaine = chaine.lower()
print(chaine.find("jette"))

chaine.replace("agacer", "énerver")
print(chaine)

print(chaine.count("pierre"))

# 4 - Modules de base

va_aleatoire = random.random()
print(va_aleatoire)

angle = 90
print(f"Le cos est : {math.cos(angle)}, et le sinus est : {math.sin(angle)}.")

print(f"{calcul_age(11, 10, 2004)} ans.")