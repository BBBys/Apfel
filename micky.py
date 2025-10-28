import logging
from genfrac1 import generate_fractal
import cv2, numpy as np
from berechnen import berBildGrenzen, berNeueBildGrenzen, berYInImag, berXInReal

def cbMaus(event, mausX, mausY, flags, param):
    global bild, zeigebild, xPixelVon, yPixelVon, xPixelBis, yPixelBis, mouse_pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        logging.debug(f"Mouse down at ({mausX},{mausY})")
        logging.debug(f"Komplex ({berXInReal(mausY)},{berYInImag(mausX)})")
        mouse_pressed = True
        xPixelVon, yPixelVon = mausX, mausY
        zeigebild = np.copy(bild)
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            # Bewegung und Taste:
            # Rechteck zeichnen
            zeigebild = np.copy(bild)
            cv2.rectangle(
                zeigebild, (xPixelVon, yPixelVon), (mausX, mausY), (0, 255, 0), 1
            )
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        xPixelBis, yPixelBis = mausX, mausY
