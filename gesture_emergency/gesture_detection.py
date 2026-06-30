import cv2
import mediapipe as mp


class HeadGestureDetector:

    def __init__(self):

        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        self.neutral_x = None
        self.neutral_y = None

        self.gesture_history = []
        self.last_direction = ""

        self.calibrated = False
        self.frame_count = 0

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.face_mesh.process(rgb)

        if not results.multi_face_landmarks:
            return None

        face = results.multi_face_landmarks[0]

        nose = face.landmark[1]

        h, w, _ = frame.shape

        x = int(nose.x * w)
        y = int(nose.y * h)

        # -------- Calibration --------

        if not self.calibrated:

            self.frame_count += 1

            self.neutral_x = x
            self.neutral_y = y

            if self.frame_count > 90:
                self.calibrated = True

            return None

        direction = None

        if x < self.neutral_x - 40:
            direction = "LEFT"

        elif x > self.neutral_x + 40:
            direction = "RIGHT"

        elif y < self.neutral_y - 25:
            direction = "UP"

        elif y > self.neutral_y + 35:
            direction = "DOWN"

        if direction:

            if direction != self.last_direction:

                self.gesture_history.append(direction)

                self.last_direction = direction

                if len(self.gesture_history) > 10:
                    self.gesture_history.pop(0)

        if len(self.gesture_history) >= 3:

            if self.gesture_history[-3:] == ["UP", "DOWN", "UP"]:

                self.gesture_history.clear()

                return "YES"

            if self.gesture_history[-3:] == ["LEFT", "RIGHT", "LEFT"]:

                self.gesture_history.clear()

                return "NO"

        return None