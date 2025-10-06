def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z*z + c
    return max_iter
s

def generate_fractal(width, height, max_iter=1000):
    # Bildbereich im komplexen Raum
    re_start, re_end = -2.0, 1.0
    im_start, im_end = -1.5, 1.5

    image = Image.new("RGB", (width, height))
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            # Umrechnung von Pixelkoordinaten in komplexe Zahlen
            c = complex(
                re_start + (x / width) * (re_end - re_start),
                im_start + (y / height) * (im_end - im_start),
            )
            m = mandelbrot(c, max_iter)
            color = 255 - int(m * 255 / max_iter)
            pixels[x, y] = (color, color, color)

    return image
