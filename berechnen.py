###
### Koordinaten
### x,y für Bild
### re,im für Berechnung
import logging

dre, dim, x0, y0, sx, sy = None, None, None, None, None, None
im_start, re_start,im_end,re_end = None,None,None, None

def berNeueGrenzen(pSy, pEy, pSx, pEx):
    re_s = berRealInX(pSx)
    re_e = berRealInX(pEx)
    im_s = berImagInY(pSy)
    im_e = berImagInY(pEy)
    berBildGrenzen(re_s, re_e, im_s, im_e)
    return

def berBildGrenzen(pRe_start, pRe_end, pIm_start, pIm_end):
    global re_end,im_end, re_start, im_start
    re_start = pRe_start
    im_start = pIm_start
    re_end = pRe_end
    im_end = pIm_end
    return 

def berPixelGrenzen(xWidth, yHeight):
    global dre, dim, x0, y0, sx, sy, im_start, re_start
    # Abstand der Pixel in Weltkoordinaten
    dre = (re_end - re_start) / xWidth
    dim = (im_end - im_start) / yHeight
    logging.debug(f"Pixelabstand: dre={dre}, dim={dim}")
    # Nullpunkte
    x0 = -re_start // dre
    y0 = -im_start // dim
    sx = 1 // dre
    sy = 1 // dim

    return dre, dim, x0, y0, sx, sy

def berImagInY(y):
    global dim, im_start
    return im_start + (y * dim)

def berRealInX(x):
    global dre, re_start
    return re_start + (x * dre)

def berYInImag(y):
    global dim, im_start
    return im_start + (y * dim)


def berXInReal(x):
    global dre, re_start
    return re_start + (x * dre)
