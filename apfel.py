import sys, logging
from PIL import Image
from genfrac1 import generate_fractal


def main(width, path, maxiter, loga, koord, statist):

    #height = int(1.5 * width)
    # 16x9-Format
    height = int(9.0/16.0 * width)

    image = generate_fractal(width, height, maxiter, loga, koord, statist)
    image.save(path)
    image.show()
    logging.info(
        f"Fraktal gespeichert als {path} ({width}x{height}), {maxiter} Iterationen"
    )


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
        default=555,
        help="max. Iterationen [555] (Grenzwert meist ab 20 erreicht)",
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
