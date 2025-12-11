# Section 1 : Imports de module
import string 

# Section 2 : Définition de fonctions

def normalise_texte(texte):
    # dictionnaire de correspondance
    lettre_convertis = {
        "À": "A", "Â": "A", "Æ": "AE", "Ç": "C",
        "É": "E", "È": "E", "Ê": "E", "Ë": "E",
        "Î": "I", "Ï": "I",
        "Ô": "O", "Œ": "OE",
        "Ù": "U", "Û": "U", "Ü": "U",
        "Ÿ": "Y",
        "à": "a", "â": "a", "æ": "ae", "ç": "c",
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "î": "i", "ï": "i",
        "ô": "o", "œ": "oe",
        "ù": "u", "û": "u", "ü": "u",
        "ÿ": "y"
    }

    resultat = ""
    for char in texte:
        if char in lettre_convertis:
            resultat += lettre_convertis[char]
        else:
            resultat += char
    
    return resultat.lower()
    
def nb_occurance_par_mot(texte):
    dico_occurance = {}

    for mot in texte.split(" "):
        if mot not in dico_occurance:
            dico_occurance[mot] = 1
        else:
            dico_occurance[mot] += 1

    return dico_occurance
    
def mot_le_plus_frequent(texte):
    dico_occurance = nb_occurance_par_mot(texte)
    mot_frequent = None
    nb_occurance_mot_frequent = 0

    for mot, val in dico_occurance.items():
        if val > nb_occurance_mot_frequent:
            nb_occurance_mot_frequent = val
            mot_frequent = mot

    return mot_frequent

def nb_vente_total(dico_vente):
    nb_vente = 0

    for val in dico_vente.values():
        nb_vente += val

    return nb_vente

def meilleur_vendeur(dico_vente):
    vendeur = None
    nb_meilleur_ventes = 0

    for nom, ventes in dico_vente.items():
        if ventes > nb_meilleur_ventes:
            nb_meilleur_ventes = ventes
            vendeur = nom

    return vendeur

def liste_triee_sans_doublon(l_entree):
    return sorted(set(l_entree))

def nb_elements(l_entree):
    return(len(set(l_entree)))

def pangramme(texte:str):
    texte = texte.lower()
    
    alphabet = set(string.ascii_lowercase)  # {'a', 'b', 'c', ..., 'z'}
    lettres = set([lettre for lettre in texte if lettre.isalpha()])
    
    return alphabet.issubset(lettres)

# Section 3 : Tests de fonctions définies et manipulations en mode "script"
print(normalise_texte("Dès Noël où un zéphyr haï me vêt de glaçons würmiens, je dîne d’exquis rôtis de bœuf au kir à l’aÿ d’âge mûr et cætera!"))
print(nb_occurance_par_mot("Je suis le plus gentil suis"))
print(mot_le_plus_frequent("Je suis le plus gentil suis suis je je je je gentil"))

ventes={"Dupont":14, "Hervy":11, "Geoffroy":15, "Layec":21}
print(nb_vente_total(ventes))
print(meilleur_vendeur(ventes))

print(liste_triee_sans_doublon(["cc", "aa", "bb", "cc", "bb", "aa"]))

print(nb_elements(["cc", "aa", "bb", "cc", "bb", "aa"]))

print(pangramme("Portez ce vieux whisky au juge blond qui fume"))
print(pangramme("Bonjour tout le monde"))