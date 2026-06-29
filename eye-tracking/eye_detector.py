import cv2


class EyeDetector:

    def __init__(self):

        # Left eye landmarks
        self.LEFT = {
            "left_corner": 33,
            "right_corner": 133,
            "upper": 159,
            "lower": 145,
            "iris": 468
        }

        # Right eye landmarks
        self.RIGHT = {
            "left_corner": 362,
            "right_corner": 263,
            "upper": 386,
            "lower": 374,
            "iris": 473
        }

    def _point(self, landmarks, index, w, h):
        lm = landmarks.landmark[index]
        return (
            int(lm.x * w),
            int(lm.y * h)
        )

    def detect(self, landmarks, w, h):

        left = {
            "left_corner": self._point(
                landmarks,
                self.LEFT["left_corner"],
                w,
                h
            ),

            "right_corner": self._point(
                landmarks,
                self.LEFT["right_corner"],
                w,
                h
            ),

            "upper": self._point(
                landmarks,
                self.LEFT["upper"],
                w,
                h
            ),

            "lower": self._point(
                landmarks,
                self.LEFT["lower"],
                w,
                h
            ),

            "iris": self._point(
                landmarks,
                self.LEFT["iris"],
                w,
                h
            )
        }

        right = {

            "left_corner": self._point(
                landmarks,
                self.RIGHT["left_corner"],
                w,
                h
            ),

            "right_corner": self._point(
                landmarks,
                self.RIGHT["right_corner"],
                w,
                h
            ),

            "upper": self._point(
                landmarks,
                self.RIGHT["upper"],
                w,
                h
            ),

            "lower": self._point(
                landmarks,
                self.RIGHT["lower"],
                w,
                h
            ),

            "iris": self._point(
                landmarks,
                self.RIGHT["iris"],
                w,
                h
            )
        }

        return {
            "left": left,
            "right": right
        }

    def draw(self, frame, eyes):

        for eye in eyes.values():

            cv2.circle(
                frame,
                eye["left_corner"],
                3,
                (255, 0, 0),
                -1
            )

            cv2.circle(
                frame,
                eye["right_corner"],
                3,
                (255, 0, 0),
                -1
            )

            cv2.circle(
                frame,
                eye["upper"],
                3,
                (0, 255, 255),
                -1
            )

            cv2.circle(
                frame,
                eye["lower"],
                3,
                (0, 255, 255),
                -1
            )

            cv2.circle(
                frame,
                eye["iris"],
                5,
                (0, 255, 0),
                -1
            )

            cv2.line(
                frame,
                eye["left_corner"],
                eye["right_corner"],
                (255, 255, 0),
                1
            )

            cv2.line(
                frame,
                eye["upper"],
                eye["lower"],
                (255, 255, 0),
                1
            )