def get_direction(x, y, width, height):

    if x < width * 0.4:
        return "LEFT"

    elif x > width * 0.6:
        return "RIGHT"

    elif y < height * 0.4:
        return "UP"

    elif y > height * 0.6:
        return "DOWN"

    return "CENTER"