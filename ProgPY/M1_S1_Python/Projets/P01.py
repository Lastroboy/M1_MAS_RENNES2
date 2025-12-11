# 22200761 Noa DELAPORTE

# Section 1 : Import de module

from P01_utils import lire_donnees, visualiser_donnees, lire_donnees_numpy
from math import *
import numpy as np
from scipy.spatial.distance import cdist

# Section 2 : Définition de fonctions

def normalise_data(X_train, X_test):
    sum_x = 0
    sum_y = 0

    for x, y in X_train:
        sum_x += x
        sum_y += y
    mean_x = sum_x / len(X_train)
    mean_y = sum_y / len(X_train)

    # Calcul des écarts-types
    sum_sq_x = 0
    sum_sq_y = 0

    for x, y in X_train:
        sum_sq_x += (x - mean_x)**2
        sum_sq_y += (y - mean_y)**2
    std_x = (sum_sq_x / len(X_train))**0.5
    std_y = (sum_sq_y / len(X_train))**0.5

    # Normalisation
    def norm(data):
        normalized = []
        for x, y in data:
            new_x = (x - mean_x) / std_x
            new_y = (y - mean_y) / std_y
            normalized.append([new_x, new_y])
        return normalized

    return norm(X_train), norm(X_test)

def normalise_data_numpy(X_train, X_test):
    mean = np.mean(X_train)
    std = np.std(X_train)
    
    X_train = (X_train - mean) / std
    X_test = (X_test - mean) / std

    return X_train, X_test

def dist(X_i, X_j):
    return sqrt(sum((xj - xi)**2 for xi, xj in zip(X_i, X_j)))

def indices_k_voisins(individu, X_train, k=2): 
    distances = []

    for i in range(len(X_train)):
        distances.append(dist(individu, X_train[i]))

    indices = np.argsort(distances)
    
    return indices[:k]

def classe_les_plus_representees(l_classes):
    nb_hommes = l_classes.count("H")
    nb_femmes = l_classes.count("F")

    return "H" if nb_hommes > nb_femmes else "F"
    
def k_plus_proches_voisins_liste(X_train, Y_train, X_test, k=1):
    predictions = []

    for individu in X_test:
        indices_voisins = indices_k_voisins(individu, X_train, k)

        classes_voisins = [Y_train[i] for i in indices_voisins]

        prediction = classe_les_plus_representees(classes_voisins)

        predictions.append(prediction)

    return predictions

def k_plus_proches_voisins_numpy(X_train, Y_train, X_test, k=1):
    distances = cdist(X_test, X_train, metric="euclidean")
    indices_voisins = np.argsort(distances, axis=1)[:, :k]
    classes_voisins = Y_train[indices_voisins]

    predictions = []    

    for voisins in classes_voisins:
        nb_hommes = np.sum(voisins == "H")
        nb_femmes = np.sum(voisins == "F")

        predictions.append("H" if nb_hommes > nb_femmes else "F")

    return predictions 

# Section 3 : Tests de fonctions définies et manipulations en mode "script"

X_train, Y_train = lire_donnees(100)
X_test, Y_test = lire_donnees(10) 

visualiser_donnees(X_train, Y_train, X_test)
print(indices_k_voisins(X_test[0], X_train, 5))
print(classe_les_plus_representees(["F", "F", "F", "H"]))
print(k_plus_proches_voisins_liste(X_train, Y_train, X_test, 3))
# print(Y_test) # Pour comparer avec les résultats obtenus précédenment

# X_train, X_test = normalise_data(X_train, X_test) # Normalisation des données via les listes..
# print(X_train, X_test)
# print(k_plus_proches_voisins_numpy(X_train, Y_train, X_test, 3)) # Verification avec les données normalisées sans numpy

###     AVEC NUMPY      ###
X_train, Y_train = lire_donnees_numpy(100)
X_test, Y_test = lire_donnees_numpy(10) 

print(k_plus_proches_voisins_numpy(X_train, Y_train, X_test, 3))

X_train, X_test = normalise_data_numpy(X_train, X_test) # Normalisation des données avec numpy
# print(X_train, X_test)
# print(k_plus_proches_voisins_numpy(X_train, Y_train, X_test, 3)) # Verification avec les données normalisées avec numpy
