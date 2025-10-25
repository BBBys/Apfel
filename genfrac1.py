### Mandelbrot-Fraktal-Generator
### Ein einfaches Beispiel zur Generierung eines Mandelbrot-Fraktals
### Bild über die Verschiebung c / Original nach Wikipedia
### https://de.wikipedia.org/wiki/Mandelbrot-Menge

import logging
from math import log10
from PIL import Image
from farbig import farbe
from iteration import mandelbrot as iterformel
import numpy as np


def generate_fractal(
    xWidth, yHeight, max_iter=1000, loga=False, koord=False, statistik=False
):
    # Bildbereich im komplexen Raum
    # real waagrecht, imag senkrecht
    # Koordinatenbereich 3.0x3.0
    # Standard:
    # re_start, re_end = -1.5, 1.5
    # im_start, im_end = -1.5, 1.5
    # 16x9-Format
    # Realteil senkrecht!
    re_start, re_end = -1.5, 1.5
    im_start, im_end = -2.2, 0.5
    # ??image = np.zeros((height,width,3), np.uint8)
    # image = Image.new("RGB", (width, height), "white")
    # pixels = image.load()
    werte = np.zeros((xWidth, yHeight), dtype=np.uint16)
    pixel = np.zeros((xWidth, yHeight, 3), dtype=np.uint8)
    logging.debug(f"werte array erstellt: {werte.shape}")
    logging.debug(f"pixel array erstellt: {pixel.shape}")

    logging.debug(f"Generiere Fraktal: xw x yh = {xWidth}x{yHeight}")
    # Abstand der Pixel in Weltkoordinaten
    dre = (re_end - re_start) / xWidth
    dim = (im_end - im_start) / yHeight
    logging.debug(f"Pixelabstand: dre={dre}, dim={dim}")
    # Nullpunkte
    #   re_start + (x * dre)=0
    #   im_start + (y * dim)=0
    #   x0=(0 - re_start)/dre
    #   y0=(0 - im_start)/dim
    x0 = -re_start // dre
    y0 = -im_start // dim
    sx = 1 // dre
    sy = 1 // dim
    logging.debug(f"Nullpunkt bei x={x0}, y={y0}")
    logging.debug(f"1-Einheit bei sx={sx}, sy={sy}")

    zstart = 0

    if statistik:
        fout = open("iters.txt", "w")
        fout.write(f"# maxiter={max_iter}\n")
        fout.write("iters;zend0;zend1;\n")
    else:
        fout = None

    for y in range(yHeight):
        y1 = im_start + (y * dim)

        for x in range(xWidth):
            x1 = re_start + (x * dre)
            # Umrechnung von Pixelkoordinaten in komplexe Zahlen
            c = complex(y1, x1)
            m, abszend0, abszend1 = iterformel(c, max_iter, zstart)
            werte[x, y] = m

    for x in range(xWidth):
        for y in range(yHeight):
            m = werte[x, y]
            # logging.debug(f"m({x},{y}): {m}")
            if fout is not None:
                fout.write(f"{m};{abszend0};{abszend1};\n")

            if loga:
                if m < 1:
                    m = 1
                f = log10(m) / log10(max_iter)
                cr = cg = cb = 255 - int(f * 255)
                pixel[x, y] = (cr, cg, cb)
            else:

                if m > max_iter - 2:
                    pixel[x][y] = [0, 0, 0]
                else:
                    pixel[x, y] = farbe(m, 4, 55)

            if koord:
                if (x - x0) % sx == 0 or (y - y0) % sy == 0:
                    pixel[x, y] = (0, 255, 0)
                if x == x0 or y == y0:
                    pixel[x, y] = (255, 0, 0)
    if fout is not None:
        fout.close()

    # if koord:
    #    if x1 % (width // 100) == 0 or y1 % (height // 10) == 0:
    #        pixels[x, y] = (255, 0, 0)
    #    if x1 == width // 2 or y1 == height // 2:
    #        pixels[x, y] = (0, 255, 0)

    return pixel
