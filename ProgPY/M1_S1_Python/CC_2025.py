
###### SECTION 1 : IMPORTS
import requests
import json
import numpy as np
from pprint import pprint

###### SECTION 2 : DEFINITION DE FONCTIONS ET DE CLASSES
# --------------- POO ----------------
"""
ModeleAffine(W, b)
- W numpy array de dimension (d,) des poids du modèle
- b scalaire de l'ordonnée à l'origine
"""
class ModeleAffine:
    def __init__(self, W, b):
        self.W = W
        self.b = b

    def __repr__(self):
        return f"Modèle affine ayant pour poids {self.W} et pour ordonnée à l'origine {self.b}"

    def predict(self, X):
        return X @ self.W + b

"""
ModeleLineaire(W) - inherit ModeleAffine
- W numpy array de dimension (d,) des poids du modèle
- L'ordonnée à l'origine est nulle
"""    
class ModeleLineaire(ModeleAffine):
    def __init__(self, W):
        super().__init__(W, 0)
    
    def __repr__(self):
        return f'Modèle Linéaire ayant pour poids {self.W}'
    
# --------------- API ----------------
""" 
isPosBounded(pos, bounds) - TRUE si pos est dans bounds
- pos : coordonnées au format [lat, long]
- bounds : objet de coordonées limites au format 
    {
        "min_lat": min_lat,
        "max_lat": max_lat,
        "min_lon": min_lon,
        "max_lon": max_lon
    }
"""   
def isPosBounded(pos, bounds):
    return pos[0] >= bounds["min_lat"] and pos[0] <= bounds["max_lat"] and pos[1] >= bounds["min_lon"] and pos[1] <= bounds["max_lon"]

"""
listGPX() - return la liste des fichiers (leurs noms) sur l'api
"""
def listGPX():
    contenu_json = requests.get("https://trails-api.onrender.com/files/", headers={'User-Agent': "Mozilla/5.0"}).json()
    return contenu_json["files"]

"""
printAllBoundingGpx(pos) - affiche via tous les fichiers dont la zone couvre la position
- pos : position au format [lat, lon]
"""
def printAllBoundingGpx(pos):
    for file in listGPX():
        contenu_json = requests.get("https://trails-api.onrender.com/files/" + file, headers={'User-Agent': "Mozilla/5.0"}).json()

        if contenu_json.get("detail", 0):
            continue # ce fichier n'a pas été trouvé sur l'API

        if isPosBounded(pos, contenu_json["bounds"]):
            print(f"Nom du fichier : {file}.\nLongueur de la trace : {contenu_json["total_distance_km"]} km.\nDénivelé positif : {contenu_json["total_ascent_m"]} m.")





###### SECTION 3 : TESTS
print("------- Exercice POO --------\n")
# Question 1:
W = np.array([1, 5, 4])
b = 2.5
m = ModeleAffine(W, b)
print(m)
# Modèle affine ayant pour poids [1 5 4] et pour ordonnée à l'origine 2.5

X = np.array([1, 5, 4])
print(m.predict(X))
# 44.5
print(50 * "-")

# Question 2:
ml = ModeleLineaire(W)
print(ml)
# Modèle Linéaire ayant pour poids [1 5 4]
print(ml.predict(X))
# 44.5

# Exercice API
# https://rtavenar.github.io/trails_api/
print("\n\n------- Exercice API --------\n")

# Question 1:
pos = [48.5713, -2.00549]
bounds = {'min_lat': 48.5713, 'max_lat': 48.68773, 'min_lon': -2.33817, 'max_lon': -2.00549}
enveloppe_resultats = isPosBounded(pos, bounds)
print(enveloppe_resultats)
# True
print(50 * "-")

# Question 2:
pprint(listGPX())
# ['endurance-trail-des-corsaires-2025.gpx',
#  'saintelyon-2025.gpx',
#  'tiger-balm-ultra-01-2024-100-km.gpx']
print(50 * "-")

# Question 3:
printAllBoundingGpx(pos)
# Nom du fichier : endurance-trail-des-corsaires-2025.gpx.
# Longueur de la trace : 101.998 km.
# Dénivelé positif : 4830.0 m.








