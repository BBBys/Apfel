### Original nach Wikipedia
### https://de.wikipedia.org/wiki/Mandelbrot-Menge

import logging
from math import log10
from PIL import Image
from farbig import farbe

# Iterationsformel:
# m, abszend0, abszend1 = iterformel(c, max_iter, zstart)
# c: Koordinaten im Bild, komplexe Zahl
# max_iter: maximale Iterationsanzahl, bis abgebrochen wird
# zstart: Startwert für z (meist 0)
#
# m: Anzahl der Iterationen bis z-Grenze erreicht
# abszend0: Betrag des vorletzten z
# abszend1: Betrag des letzten z


def mandelbrot(c, max_iter, z1=0):
    absmax = 1000.0
    z0 = 0.0
    for n in range(max_iter):
        if abs(z1) > absmax:
            # setzt man max_iter auf 100, Grenze auf > 1000
            # ist der Abbruchwert in 75% der Fälle
            # nach 11 Iterationen erreicht
            return n, abs(z0), abs(z1)
        z0 = z1
        z1 = z1 * z1 + c
    # if abs(z) > absmax:print(z,abs(z),n)
    return max_iter - 1, abs(z0), abs(z1)


def mb2(c, max_iter, z1=0):
    absmax = 1000.0
    z0 = 0.0  # nur für erste Ausgabe
    for n in range(max_iter):
        if abs(z1) > absmax:
            # setzt man max_iter auf 100, Grenze auf > 1000
            # ist der Abbruchwert in 75% der Fälle
            # nach 11 Iterationen erreicht
            return n, abs(z0), abs(z1)
        z0 = z1
        z1 = z1 * z1 + c
    # if abs(z) > absmax:print(z,abs(z),n)
    return max_iter - 1, abs(z0), abs(z1)
