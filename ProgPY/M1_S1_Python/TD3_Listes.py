# Section 1 : Imports de module
import math

# Section 2 : Définition de fonctions

def print_sinus():
    liste_angle_sinus = []
    for angle_deg in range(360):
        angle_rad = angle_deg*2*math.pi/360
        sinus = math.sin(angle_rad)
        liste_angle_sinus.append([angle_rad, sinus])
    print(liste_angle_sinus)

def plusieurs_tables(l_bases):
    t_multiplication = []

    for i, val in enumerate(l_bases):
        t_bases = []
        for i in range(1, 11):
            t_bases.append(val*i)
            
        t_multiplication.append(t_bases)

    return t_multiplication

def intervalle(borne_inf, borne_sup, puissance):
    l_intervalle = []

    for i in range(borne_inf, borne_sup+1):
        l_intervalle.append(i**puissance)

    return l_intervalle

def intervalle_au_carre(borne_inf, borne_sup):
    return intervalle(borne_inf, borne_sup, 2)

def taille_chaine(l_chaines):
    l_taille_chaine = []

    for chaine in l_chaines:
        l_taille_chaine.append(len(chaine))

    return l_taille_chaine

def liste_triee_sans_doublon(l_entree):
    l_sortie = []
    for elem in l_entree:
        if elem not in l_sortie:
            l_sortie.append(elem)
    return sorted(l_sortie)

def mot_le_plus_long(chaine:str):
    mot_long = None
    nb_caractere = 0

    l_chaine = chaine.split(" ")

    for elem in l_chaine:
        if len(elem) > nb_caractere:
            nb_caractere = len(elem)
            mot_long = elem

    return mot_long

def valeurs_paires(l_entree):
    l_sortie = []

    for val in l_entree:
        if val % 2 == 0:
            l_sortie.append(val)

    return l_sortie

def ajouter_3(l_entree):
    return [(val+3) for val in l_entree]

def liste_reels(chaine:str):
    return [float(val) for val in chaine.split(" ")]


# Section 3 : Tests de fonctions définies et manipulations en mode "script"

# print_sinus()
print(plusieurs_tables([2, 5]))
print(intervalle(2, 6, 2))
print(intervalle_au_carre(2, 8))
print(taille_chaine(["coucou", "bonjour", "Noa", ""]))
print(liste_triee_sans_doublon(["cc", "aa", "bb", "cc", "bb", "aa"]))
print(mot_le_plus_long("coucou noa le bricoleur"))
print(valeurs_paires([2, 5, 7, 6]))
print(ajouter_3([2, 5, 7]))
print(liste_reels("1.0 3.14 7 8.4 0.0"))

