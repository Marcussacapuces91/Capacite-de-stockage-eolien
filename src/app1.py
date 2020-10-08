#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import math

from matplotlib import pyplot

def generateurWeibull(A = 6.0, k = 2.0):
    while True:
        v = random.random() * 50
        w = k * (v / A)**(k-1) * math.exp(-(v / A)**k) / A
        if random.random() < w:
            yield(v)
    
def filtreAeroGenerateur(v, vMin = 6, vSat = 15, vMax = 25, pMax = 5):
    """Calcule la puissance produite en fonction de la vitesse indiquée et des paramètres du générateur"""
    if v < vMin or v > vMax:
        return 0
    if v > vSat:
        return pMax
    a = pMax / (vSat ** 3)
    return a * (v ** 3)
    
    
    
if __name__ == "__main__":
    
#    pyplot.plot([1, 3, 2, 3], [4, 8, 5, 4], linestyle = 'none', marker = 'o', c = 'lime',
#      markersize = 10)
#    pyplot.xlim(0, 4)
#    pyplot.ylim(0, 10)
#    pyplot.title('Avec des points seulement')   
#    pyplot.plot(2,5, linestyle='none', marker='o')
#    pyplot.show()
    
    for v in generateurWeibull():
        p = filtreAeroGenerateur(v)
        print(f"{round(v*3600/1000)} km/h", f"{round(p*1000)} kW", f"{round(100*p/5)}%")
    