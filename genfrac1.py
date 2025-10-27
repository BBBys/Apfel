### Mandelbrot-Fraktal-Generator
### Ein einfaches Beispiel zur Generierung eines Mandelbrot-Fraktals
### Bild über die Verschiebung c / Original nach Wikipedia
### https://de.wikipedia.org/wiki/Mandelbrot-Menge

import logging
from math import log10
from PIL import Image
from farbig import farbe
from iteration import mb0 as iterformel
from berechnen import berPixelGrenzen, berImagInY, berRealInX, berYInImag, berXInReal
import numpy as np


def generate_fractal(
    xWidth,
    yHeight,
    max_iter=1000,
    loga=False,
    koord=False,
    statistik=False,
):
    # Bildbereich im komplexen Raum
    # real waagrecht, imag senkrecht
    # Koordinatenbereich 3.0x3.0
    # Standard:
    # re_start, re_end = -1.5, 1.5
    # im_start, im_end = -1.5, 1.5
    # 16x9-Format
    # Realteil senkrecht!

    werte = np.zeros((xWidth, yHeight), dtype=np.uint16)
    pixel = np.zeros((xWidth, yHeight, 3), dtype=np.uint8)
    #logging.debug(f"werte array erstellt: {werte.shape}")
    #logging.debug(f"pixel array erstellt: {pixel.shape}")

    logging.debug(f"Generiere Fraktal: xw x yh = {xWidth}x{yHeight}")
    dre, dim, x0, y0, sx, sy = berPixelGrenzen(xWidth, yHeight)

    logging.debug(f"Nullpunkt bei x={x0}, y={y0}")
    logging.debug(f"1-Einheit bei sx={sx}, sy={sy}")

    zstart = 0

    if statistik:
        fout = open("iters.txt", "w")
        fout.write(f"# maxiter={max_iter}\n")
        fout.write("iters;zend0;zend1;\n")
    else:
        fout = None

    for yPixel in range(yHeight):
        imag = berYInImag(yPixel)
        for xPixel in range(xWidth):
            real = berXInReal(xPixel)
            # Umrechnung von Pixelkoordinaten in komplexe Zahlen
            c = complex(imag, real)
            m, abszend0, abszend1 = iterformel(c, max_iter, zstart)
            werte[xPixel, yPixel] = m
            if fout is not None:
                fout.write(f"{m};{abszend0};{abszend1};\n")

    for xPixel in range(xWidth):
        for yPixel in range(yHeight):
            m = werte[xPixel, yPixel]
            # logging.debug(f"m({x},{y}): {m}")

            if loga:
                if m < 1:
                    m = 1
                f = log10(m) / log10(max_iter)
                cr = cg = cb = 255 - int(f * 255)
                pixel[xPixel, yPixel] = (cr, cg, cb)
            else:

                if m > max_iter - 2:
                    pixel[xPixel][yPixel] = [0, 0, 0]
                else:
                    pixel[xPixel, yPixel] = farbe(m, 4, 55)

            if koord:
                if (xPixel - x0) % sx == 0 or (yPixel - y0) % sy == 0:
                    pixel[xPixel, yPixel] = (0, 255, 0)
                if xPixel == x0 or yPixel == y0:
                    pixel[xPixel, yPixel] = (255, 0, 0)
    if fout is not None:
        fout.close()

    # if koord:
    #    if x1 % (width // 100) == 0 or y1 % (height // 10) == 0:
    #        pixels[x, y] = (255, 0, 0)
    #    if x1 == width // 2 or y1 == height // 2:
    #        pixels[x, y] = (0, 255, 0)

    return pixel
