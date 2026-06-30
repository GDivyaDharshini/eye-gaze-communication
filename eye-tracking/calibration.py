class Calibration:

    def __init__(self):

        self.horizontal_offset = 0.0
        self.vertical_offset = 0.0

        self.samples = 0

    def update(self, eyes, pitch, yaw):

        left = eyes["left"]
        right = eyes["right"]

        # ----- Left eye -----
        lx = left["left_corner"][0]
        rx = left["right_corner"][0]
        ix = left["iris"][0]

        uy = left["upper"][1]
        dy = left["lower"][1]
        iy = left["iris"][1]

        if rx != lx:
            h = (ix - lx) / (rx - lx)
        else:
            h = 0.5

        if dy != uy:
            v = (iy - uy) / (dy - uy)
        else:
            v = 0.5

        # Running average
        self.horizontal_offset = (
            self.horizontal_offset * self.samples + h
        ) / (self.samples + 1)

        self.vertical_offset = (
            self.vertical_offset * self.samples + v
        ) / (self.samples + 1)

        self.samples += 1

    def correct_horizontal(self, value):
        return value - self.horizontal_offset + 0.5

    def correct_vertical(self, value):
        return value - self.vertical_offset + 0.5

    def reset(self):
        self.horizontal_offset = 0.0
        self.vertical_offset = 0.0
        self.samples = 0