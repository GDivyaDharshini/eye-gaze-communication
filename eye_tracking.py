import cv2
import mediapipe as mp


class EyeTracker:

    def __init__(self):

        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def detect(self, frame):

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        result = self.face_mesh.process(rgb)

        if not result.multi_face_landmarks:
            return "CENTER", False

        face = result.multi_face_landmarks[0]

        # Eye landmarks
        left_corner = face.landmark[33]
        right_corner = face.landmark[133]

        top_lid = face.landmark[159]
        bottom_lid = face.landmark[145]

        iris = face.landmark[468]

        # -------------------------
        # Blink Detection
        # -------------------------

        eye_opening = abs(
            bottom_lid.y - top_lid.y
        )

        blink = eye_opening < 0.008

        # -------------------------
        # Horizontal Detection
        # -------------------------

        eye_width = (
            right_corner.x - left_corner.x
        )

        if eye_width == 0:
            return "CENTER", blink

        horizontal_ratio = (
            iris.x - left_corner.x
        ) / eye_width

        # -------------------------
        # Vertical Detection
        # -------------------------

        eye_height = (
            bottom_lid.y - top_lid.y
        )

        if eye_height == 0:
            return "CENTER", blink

        vertical_ratio = (
            iris.y - top_lid.y
        ) / eye_height

        direction = "CENTER"

        if vertical_ratio < 0.35:
            direction = "UP"

        elif vertical_ratio > 0.70:
            direction = "DOWN"

        elif horizontal_ratio < 0.35:
            direction = "LEFT"

        elif horizontal_ratio > 0.65:
            direction = "RIGHT"

        return direction, blink