### Mandelbrot-Fraktal-Generator
### Ein einfaches Beispiel zur Generierung eines Mandelbrot-Fraktals
### Bild über die Verschiebung c / Original nach Wikipedia
### https://de.wikipedia.org/wiki/Mandelbrot-Menge

from math import log10
from PIL import Image

def mandelbrot(c, max_iter,z=0):
    for n in range(max_iter):
        if abs(z) > 1000:
            return n
        z = z *z + c
    return max_iter


def generate_fractal(width, height, max_iter=1000,loga=False):
    # Bildbereich im komplexen Raum
    re_start, re_end = -2.0, 1.0
    im_start, im_end = -1.5, 1.5

    image = Image.new("RGB", (width, height))
    pixels = image.load()

    dre= (re_end - re_start)/ width
    dim= (im_end - im_start)/height
    for x in range(width):
        for y in range(height):
            # Umrechnung von Pixelkoordinaten in komplexe Zahlen
            c = complex(
                re_start + (x*dre),
                im_start + (y*dim)
            )
            m = mandelbrot(c, max_iter)

            if loga:
                if m<1: m=1
                f=log10(m)/ log10(max_iter)
                color = 255 - int(f * 255)
            else:
                color = 255 - int(m * 255 / max_iter)
            pixels[x, y] = (color, color, color)

    return image
