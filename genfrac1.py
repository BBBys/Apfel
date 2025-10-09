### Mandelbrot-Fraktal-Generator
### Ein einfaches Beispiel zur Generierung eines Mandelbrot-Fraktals
### Bild über die Verschiebung c / Original nach Wikipedia
### https://de.wikipedia.org/wiki/Mandelbrot-Menge

import logging
from math import log10
from PIL import Image


def mandelbrot(c, max_iter, z1=0):
    absmax=1000.0
    z0=0.0
    for n in range(max_iter):
        if abs(z1) >absmax:
            # setzt man max_iter auf 100, Grenze auf > 1000
            # ist der Abbruchwert in 75% der Fälle
            # nach 11 Iterationen erreicht
            return n, abs(z0),abs(z1)
        z0=z1
        z1 = z1 * z1 + c
    #if abs(z) > absmax:print(z,abs(z),n)
    return max_iter-1, abs(z0),abs(z1)


def generate_fractal(
    width, height, max_iter=1000, loga=False, koord=False, statistik=False
):
    # Bildbereich im komplexen Raum
    re_start, re_end = -2.0, 1.0
    im_start, im_end = -1.5, 1.5

    image = Image.new("RGB", (width, height), "white")
    pixels = image.load()
    # Abstand der Pixel in Weltkoordinaten
    dre = (re_end - re_start) / width
    dim = (im_end - im_start) / height
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

    for x in range(width):
        x1 = re_start + (x * dre)
        for y in range(height):
            y1 = im_start + (y * dim)
            # Umrechnung von Pixelkoordinaten in komplexe Zahlen
            c = complex(x1, y1)
            m, abszend0, abszend1 = mandelbrot(c, max_iter, zstart)
            if fout is not None:
                fout.write(f"{m};{abszend0};{abszend1};\n")

            if loga:
                if m < 1:
                    m = 1
                f = log10(m) / log10(max_iter)
                cr = cg = cb = 255 - int(f * 255)
            else:
                # cr=cb=cg = 255 - int(m * 255 / max_iter)
                cr = cb = cg = 255
                if m > 4:
                    cr, cg, cb = 255, 60, 0  # rot        10%
                if m > 5:
                    cr, cg, cb = 255, 255, 0  # gelb       25%
                if m > 6:
                    cr, cg, cb = 0, 255, 0  # grün       50%
                if m > 10:
                    cr, cg, cb = 0, 0, m * 24  # blau       75%
                if m > 29:
                    # Grenzwert wahrscheinlich erreicht
                    #cr, cg, cb = 0, 0, 0  # schwarz    90%
                    c=int(200*abszend1)
                    cr=cg=cb=c%256
                    
            pixels[x, y] = (cr, cg, cb)
            if koord:
                if (x - x0) % sx == 0 or (y - y0) % sy == 0:
                    pixels[x, y] = (0, 255, 0)
                if x == x0 or y == y0:
                    pixels[x, y] = (255, 0, 0)
    if fout is not None:
        fout.close()

    # if koord:
    #    if x1 % (width // 100) == 0 or y1 % (height // 10) == 0:
    #        pixels[x, y] = (255, 0, 0)
    #    if x1 == width // 2 or y1 == height // 2:
    #        pixels[x, y] = (0, 255, 0)

    return image
