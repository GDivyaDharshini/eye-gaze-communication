import math


class HeadPoseEstimator:

    def __init__(self):
        pass

    def _point(self, landmarks, index, w, h):
        lm = landmarks.landmark[index]
        return (
            int(lm.x * w),
            int(lm.y * h)
        )

    def estimate(self, landmarks, w, h):

        # MediaPipe landmarks
        nose = self._point(landmarks, 1, w, h)

        left_eye = self._point(landmarks, 33, w, h)
        right_eye = self._point(landmarks, 263, w, h)

        chin = self._point(landmarks, 152, w, h)

        lx, ly = left_eye
        rx, ry = right_eye
        nx, ny = nose
        cx, cy = chin

        # ---------- Yaw (left/right head rotation) ----------
        eye_center_x = (lx + rx) / 2
        yaw = nx - eye_center_x

        # ---------- Pitch (up/down head movement) ----------
        face_height = abs(cy - ny)

        if face_height == 0:
            face_height = 1

        eye_center_y = (ly + ry) / 2

        pitch = (eye_center_y - ny) / face_height

        # ---------- Roll (head tilt) ----------
        roll = math.degrees(math.atan2(
            ry - ly,
            rx - lx
        ))

        return pitch * 100, yaw, roll