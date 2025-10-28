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

def main(width, path, maxiter, loga, koord, statist):
    global bild, zeigebild, xPixelVon, yPixelVon, xPixelBis, yPixelBis, mouse_pressed

    # height = int(1.5 * width)
    # 16x9-Format
    height = int(9.0 / 16.0 * width)
    re_start, re_end = -1.5, 1.5
    im_start, im_end = -2.2, 0.5
    berBildGrenzen(re_start, re_end, im_start, im_end)

    weiter = True
    while weiter:
        bild = generate_fractal(height, width, maxiter, loga, koord, statist)
        # bild.write(path)
        # logging.info(
        #    f"Fraktal gespeichert als {path} ({width}x{height}), {maxiter} Iterationen"
        # )

        mouse_pressed = False
        xPixelVon = yPixelVon = xPixelBis = yPixelBis = -1
        cv2.namedWindow("guiBild", cv2.WINDOW_FULLSCREEN)
        cv2.setMouseCallback("guiBild", cbMaus)
        zeigebild = np.copy(bild)

        while True:
            cv2.imshow("guiBild", zeigebild)
            k = cv2.waitKey(1)
            if k == ord("c"):
                if yPixelVon > yPixelBis:
                    yPixelVon, yPixelBis = yPixelBis, yPixelVon
                if xPixelVon > xPixelBis:
                    xPixelVon, xPixelBis = xPixelBis, xPixelVon
                if yPixelBis - yPixelVon > 1 and xPixelBis - xPixelVon > 0:
                    bild = bild[yPixelVon:yPixelBis, xPixelVon:xPixelBis]
                    zeigebild = np.copy(bild)
            elif k == 27:
                weiter = False
                break
            elif k == ord("r"):
                # neues Bild (Re, Im) aus Pixeln (x, y) berechnen
                #Komplex ({berXInReal(mausY)},{berYInImag(mausX)})")
                imVon = berYInImag(xPixelVon)
                imBis = berYInImag(xPixelBis)
                reVon = berXInReal(yPixelVon)
                reBis = berXInReal(yPixelBis)
                logging.debug(
                    f"Pixel: x: {xPixelVon}..{xPixelBis}, y: {yPixelVon}..{yPixelBis}"
                )
                logging.debug(f"Bild: re: {reVon}..{reBis}, im: {imVon}..{imBis}")
                berNeueBildGrenzen(xPixelVon, xPixelBis, yPixelVon, yPixelBis)
                weiter = True
                break
        cv2.destroyAllWindows()
    # while weiter

    # cv2.imshow("Original image",bild)
    # cv2.waitKey(0)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="Apfel",
        description="...zeichnen eines Apfelmännchen-Fraktals",
    )
    parser.add_argument(
        "-l", "--loga", dest="pLOGA", action="store_true", help="Log-Farb-Darstellung"
    )
    parser.add_argument(
        "-v", "--verbose", dest="pVerbose", action="store_true", help="Debug-Ausgabe"
    )
    parser.add_argument(
        "-s",
        "--statistik",
        dest="pStat",
        action="store_true",
        help="Ausgabe für Statistik",
    )
    parser.add_argument(
        "-k",
        "--koordinaten",
        dest="pKoord",
        action="store_true",
        help="mit Koordinaten",
    )
    parser.add_argument("-w", dest="w", nargs="?", default=200, help="Breite")
    parser.add_argument(
        "-m",
        dest="m",
        nargs="?",
        default=20,
        help="max. Iterationen [20] (Grenzwert meist ab 20 erreicht)",
    )
    parser.add_argument(
        "path", nargs="?", default="./bild.png", help="Dateiname für das Bild"
    )
    arguments = parser.parse_args()
    pWIDTH = int(arguments.w)
    pMAX = int(arguments.m)
    pPATH = arguments.path
    loga = arguments.pLOGA
    pKOORD = arguments.pKoord
    pSTAT = arguments.pStat

    if arguments.pVerbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logging.info("Starte Mandelbrot-Fraktal-Generierung")
    main(pWIDTH, pPATH, pMAX, loga, pKOORD, pSTAT)
#
# Für eine Animation des Apfelmännchen-Fraktals gibt es einige spannende Möglichkeiten, die du auf dem Raspberry Pi umsetzen kannst. Hier sind ein paar kreative Ansätze:
#
# 🎞️ 1. Zoom-Animation ins Fraktal
# Du kannst eine Sequenz von Bildern erzeugen, die schrittweise in einen interessanten Bereich des Fraktals hineinzoomen.
#
# Idee:
#
#    Wähle einen Punkt im Fraktal (z. B. -0.75 + 0.1i)
#    Erzeuge Bilder mit immer kleinerem Ausschnitt um diesen Punkt
#    Speichere die Bilder als PNGs und erstelle daraus ein Video (z. B. mit ffmpeg)
#
# Code-Skizze:
# python for i in range(100): zoom = 1.5 / (1.05 i) restart = centerx - zoom reend = centerx + zoom imstart = centery - zoom imend = centery + zoom # generate_fractal(...) mit diesen Werten
#
# 🌈 2. Farbverlauf-Animation
# Statt Graustufen kannst du die Iterationsanzahl in Farben umwandeln und diese über die Zeit verändern.
#
# Idee:
#
#    Nutze z. B. HSV-Farben, deren Farbton sich pro Frame ändert
#    Erzeuge eine „pulsierende“ oder „rotierende“ Farbwelt
#
# 🌀 3. Parameter-Variation
# Du kannst die Iterationsgrenze oder die Formel leicht verändern, um dynamische Effekte zu erzeugen.
#
# Beispiel:
#
#    Iterationsanzahl von 50 bis 1000 steigern
#    Alternative Formel: ( z = z^2 + c ) → ( z = z^3 + c ) oder andere Varianten
