# Section 1 : Imports de module
import numpy as np

# Section 2 : Définition de fonctions

# Section 3 : Tests de fonctions définies et manipulations en mode "script"
v = np.array([0, 0, 0, 0])
print(v)

I_4 = np.eye(4)
print(I_4)

M = np.arange(12) # équivalent d'un range 
M = M.reshape((3, 4)) # redimensionner en x lignes et y colonnes
print(M)

M_T = M.T
print(M_T)

M2 = np.ones((10,10))
M2[1:-1,1:-1] = 0
print(M2)

M_r = np.random.randn(10, 10)
print(M_r)

M_std = (M_r - M_r.min()) / (M_r.max() - M_r.min())
print(M_std)

M_I = M @ I_4           # produit matriciel
M_I_v = M_I + v         # ajout du vecteur v
print(M_I)
print(M_I_v)

x = np.array([0.1, 0.2, 0.4])
y = np.array([1., 2., 8.])

C = 1 / (x - y)
print(C)

M_r2 = np.random.random((10, 3))
print(M_r2)
M_centered = M_r2 - M_r2.mean(axis=1, keepdims=True)
print(M_centered)
print(M_centered[0].sum()) # on est proche de 0

notes = np.array(
[[10, 12],
[15, 16],
[18, 12]]
)

moyenne_etudiants = notes.mean(axis=0)
print(moyenne_etudiants)

nb_notes_sup_12 = (notes > 12).sum()
print(nb_notes_sup_12)

M = np.eye(10)
mcol = np.arange(10)
mrow = np.arange(10)
mrow = mrow.T
print(M * mrow * mcol)