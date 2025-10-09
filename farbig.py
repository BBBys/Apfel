import colorsys

def farbe(iter,imin=4.0,imax=24.0):
    # iter von 1 bis 24
    # Convert Iterationen in HSV to RGB
    # H: 0=rot, 0.33=grün, 0.66=blau, 1=rot
    # S: 1  V: 1
    if iter < imin:     iter = 1
    if iter > imax:     iter = imax
    
    sat=.8
    val=.99

    hue = (iter / imax)*.75

    rgb = colorsys.hsv_to_rgb(iter/imax,sat,val)
    # Scale RGB values to the range [0, 255]
    rgb_scaled = tuple(int(c * 255) for c in rgb)

    return rgb_scaled