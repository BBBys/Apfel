###
### Koordinaten
### x,y für Bild
### re,im für Berechnung
import logging

xPixelProReal, yPixelProImag, xPixelReal0, yPixelImag0, sx, sy = None, None, None, None, None, None
im_start, re_start, im_end, re_end = None, None, None, None


def berNeueBildGrenzen(pSy, pEy, pSx, pEx):
    re_s = berXInReal(pSx)
    re_e = berXInReal(pEx)
    im_s = berYInImag(pSy)
    im_e = berYInImag(pEy)
    berBildGrenzen(re_s, re_e, im_s, im_e)
    return


def berBildGrenzen(pRe_start, pRe_end, pIm_start, pIm_end):
    global re_end, im_end, re_start, im_start
    re_start = pRe_start
    im_start = pIm_start
    re_end = pRe_end
    im_end = pIm_end
    logging.debug(
        f"Neue Bildgrenzen gesetzt: re: {re_start}..{re_end}, im: {im_start}..{im_end}"
    )
    return


def berPixelGrenzen(xWidth, yHeight):
    global xPixelProReal, yPixelProImag, xPixelReal0, yPixelImag0, sx, sy, im_start, re_start
    # Abstand der Pixel in Weltkoordinaten
    xPixelProReal = (re_end - re_start) / xWidth
    yPixelProImag = (im_end - im_start) / yHeight
    #logging.debug(f"Pixelabstand: dre={xPixelProReal}, dim={yPixelProImag}")
    # Nullpunkte
    xPixelReal0 = -re_start / xPixelProReal
    yPixelImag0 = -im_start / yPixelProImag
    sx = 1 / xPixelProReal
    sy = 1 / yPixelProImag

    return xPixelProReal, yPixelProImag, xPixelReal0, yPixelImag0, sx, sy


def berImagInY(imag):
    global yPixelProImag, im_start
    return (imag - im_start) / yPixelProImag


def berRealInX(real):
    global xPixelProReal, re_start
    return (real - re_start) / xPixelProReal


def berYInImag(y):
    global yPixelProImag, im_start
    return im_start + (y * yPixelProImag)


def berXInReal(x):
    global xPixelProReal, re_start
    return re_start + (x * xPixelProReal)
