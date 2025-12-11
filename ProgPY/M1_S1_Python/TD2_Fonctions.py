# Section 1 : Imports de module
# Section 2 : Définition de fonctions

# 2 - Exercices indépendants
def compte_mots(chaine:str):
    mots = chaine.split(sep=" ")

    return len(mots)

def est_un_fichier_texte(nom_fichier:str):
    # format = [".txt", ".csv", ".json"]
    # for nom_format in format:
    #     return nom_format in nom_fichier

    extensions = (".txt", ".csv", ".json")
    return nom_fichier.endswith(extensions)

def table_multiplication(base:int, dmultiplicateur:int, fmultiplicateur:int):
    for i in range(dmultiplicateur, fmultiplicateur+1):
        print(f"{base}*{i}={base*i}")

def nb_annees_production():
    masse_grain_g = 0.035  # masse d'un grain en grammes
    production_annuelle_g = 650 * 10**12  # production annuelle mondiale en grammes

    # Nombre de grains demandés par Sessa
    nb_grains = 2**64 - 1

    # Masse totale demandée en grammes
    masse_totale_g = nb_grains * masse_grain_g

    # Nombre d'années nécessaires
    nb_annees = masse_totale_g / production_annuelle_g

    return nb_annees

def date_lendemain(jour:int, mois:int, annee:int):
    jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Vérification année bissextile
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        jours_par_mois[1] = 29  # février = 29 jours

    # Passage au jour suivant
    jour += 1

    if jour > jours_par_mois[mois - 1]:
        jour = 1
        mois += 1
        if mois > 12:
            mois = 1
            annee += 1

    return (jour, mois, annee)

def table_multiplication_usuelle(base):
    return table_multiplication(base, 1, 10)

def nb_occurence(s:str, let:str):
    return s.count(let.upper())

def nb_occurence_A(s:str):
    return nb_occurence(s, "A")


# Section 3 : Tests de fonctions définies et manipulations en mode "script"

phrase = "Bonjour, je m'appelle Noa Delaporte."
print(compte_mots(phrase))

mon_fichier = "coucou.txt"
# mon_fichier = "coucou.pap"
print(est_un_fichier_texte(mon_fichier))

table_multiplication(5, 4, 7)

print(f"Nombre d'années de production nécessaires : {nb_annees_production():.2f} ans")

print(date_lendemain(28, 2, 2023))  # (1, 3, 2023) année non bissextile)
print(date_lendemain(28, 2, 2024))  # (29, 2, 2024) année bissextile
print(date_lendemain(31, 12, 2024)) # (1, 1, 2025)

table_multiplication_usuelle(5)

phrase = "Bonjour, je m'appelle Noa Delaporte."
print(nb_occurence(phrase, "a"), nb_occurence(phrase, "A"))
print(nb_occurence(phrase, "B"), nb_occurence(phrase, "b"))

phrase = "Bonjour, je m'Appelle NoA Delaporte."
print(nb_occurence_A(phrase))


 

def indice_max_a(chn):
    pos_max_A = None
    nb_max_A = 0

    for i, val in enumerate(chn):
        if val.count("A") > nb_max_A:
            nb_max_A = val.count("A")
            pos_max_A = i

    return pos_max_A


print(indice_max_a(["AAAAA", "AAA"]))