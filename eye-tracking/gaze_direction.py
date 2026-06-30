import math


class GazeTracker:

    def __init__(self):

        # Default thresholds
        self.left_threshold = 0.35
        self.right_threshold = 0.65

        self.up_threshold = 0.35
        self.down_threshold = 0.65

        # Eye closed threshold
        self.closed_threshold = 6

    def eye_ratio(self, eye):

        lx, ly = eye["left_corner"]
        rx, ry = eye["right_corner"]

        ux, uy = eye["upper"]
        dx, dy = eye["lower"]

        ix, iy = eye["iris"]

        eye_width = abs(rx - lx)
        eye_height = abs(dy - uy)

        if eye_width == 0:
            eye_width = 1

        if eye_height == 0:
            eye_height = 1

        horizontal = (ix - lx) / eye_width
        vertical = (iy - uy) / eye_height

        return horizontal, vertical, eye_height

    def predict(self, eyes, pitch, yaw, calibration):

        # Left eye
        h1, v1, eh1 = self.eye_ratio(eyes["left"])

        # Right eye
        h2, v2, eh2 = self.eye_ratio(eyes["right"])

        # Average values
        horizontal = (h1 + h2) / 2
        vertical = (v1 + v2) / 2

        eye_open = (eh1 + eh2) / 2

        # -----------------------------
        # Closed eyes = DOWN
        # -----------------------------
        if eye_open < self.closed_threshold:
            return "DOWN"

        # Head compensation
        horizontal -= yaw * 0.002
        vertical += pitch * 0.002

        # Calibration
        horizontal = calibration.correct_horizontal(horizontal)
        vertical = calibration.correct_vertical(vertical)

        # Horizontal direction
        if horizontal < self.left_threshold:
            return "LEFT"

        elif horizontal > self.right_threshold:
            return "RIGHT"

        # Vertical direction
        elif vertical < self.up_threshold:
            return "UP"

        elif vertical > self.down_threshold:
            return "DOWN"

        else:
            return "CENTER"