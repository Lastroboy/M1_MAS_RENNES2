# Imports
from math import *
# Classes et Fonctions
class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __repr__(self):
        return f'Point(x={self.x},y={self.y})'
    
    def distance(self, autre_point):
        return sqrt((self.x - autre_point.x)**2 + (self.y - autre_point.y)**2)

class Intervalle:
    def __init__(self, debut, fin):
        self.debut = debut
        self.fin = fin

    
    def __contains__(self, v):
        if v in range(self.debut, self.fin+1):
            return True
        return False

class Fraction:
    def __init__(self, numerateur=1, denominateur=1):
        if denominateur == 0:
            raise ValueError("Le dénominateur ne peut pas être nul.")
        
        if numerateur * denominateur >= 0:
            self.signe = +1
        else:
            self.signe = -1
        
        self.num = abs(numerateur)
        self.den = abs(denominateur)

    def __repr__(self):
        prefix = "-" if self.signe == -1 else ""
        return f"({prefix}{self.num}/{self.den})"
    
    def __neg__(self):
        return Fraction(-1 * self.signe * self.num, self.den)
    
    def __add__(self, other):
        return Fraction(self.signe * other.signe * (self.num * other.den + other.num * self.den), self.den * other.den)
    
    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, other):
        return Fraction(self.signe * other.signe * self.num * other.num, self.den * other.den)


# Tests

point1 = Point(1, 6)
point2 = Point(1, 3)

print(point1.distance(point2))

intervalle1 = Intervalle(10, 20)
print(21 in intervalle1)


f0 = Fraction(1, 5)
f1 = Fraction(2, 3)
print(-f0)
print(f0 + f1)
print(f0 * f1)
print(f0 - f1)


