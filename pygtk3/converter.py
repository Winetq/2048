def convert_hex_to_rgb(s):
    rgb = []
    for i in (0, 2, 4):
        decimal = int(s[i:i+2], 16)
        rgb.append(decimal)

    return tuple(rgb)
