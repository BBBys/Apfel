### Mandelbrot-Fraktal-Generator
### Ein einfaches Beispiel zur Generierung eines Mandelbrot-Fraktals
### Bild über die Verschiebung c / Original nach Wikipedia
### https://de.wikipedia.org/wiki/Mandelbrot-Menge

import logging
from math import log10
from PIL import Image


def mandelbrot(c, max_iter, z=0):
    for n in range(max_iter):
        if abs(z) > 1000:
            return n
        z = z * z + c
    return max_iter


def generate_fractal(width, height, max_iter=1000, loga=False,koord=False):
    # Bildbereich im komplexen Raum
    re_start, re_end = -2.0, 1.0
    im_start, im_end = -1.5, 1.5

    image = Image.new("RGB", (width, height),"white")
    pixels = image.load()
    #Abstand der Pixel in Weltkoordinaten
    dre = (re_end - re_start) / width
    dim = (im_end - im_start) / height
    logging.debug(f"Pixelabstand: dre={dre}, dim={dim}")
    #Nullpunkte
    #   re_start + (x * dre)=0
    #   im_start + (y * dim)=0
    #   x0=(0 - re_start)/dre
    #   y0=(0 - im_start)/dim
    x0= -re_start//dre
    y0= -im_start//dim
    sx=sy=10
    print(f"Nullpunkt bei x={x0}, y={y0}"   )
    zstart = 0
    for x in range(width):
        x1=re_start + (x * dre)
        for y in range(height):
            y1= im_start + (y * dim)
            # Umrechnung von Pixelkoordinaten in komplexe Zahlen
            c = complex(x1,y1)
            m = mandelbrot(c, max_iter, zstart)

            if loga:
                if m < 1:
                    m = 1
                f = log10(m) / log10(max_iter)
                color = 255 - int(f * 255)
            else:
                color = 255 - int(m * 255 / max_iter)
            pixels[x, y] = (color, color, color)
            if x== x0 or y == y0:
                pixels[x, y] = (255, 0, 0)
            if (x-x0)%sx== 0 or (y-y0)%sy == 0:
                pixels[x, y] = (255, 0, 0)
            

            #if koord:
            #    if x1 % (width // 100) == 0 or y1 % (height // 10) == 0:
            #        pixels[x, y] = (255, 0, 0)
            #    if x1 == width // 2 or y1 == height // 2:
            #        pixels[x, y] = (0, 255, 0)  

    return image
