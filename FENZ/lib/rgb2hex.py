def rgb2hex(r,g,b):
    "transform a triplet r, g, b to hex color"

    def clamp(x):
        return max(0, min(x, 255))

    h = "#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b))

    return h
