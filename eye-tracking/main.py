import cv2
import mediapipe as mp
import numpy as np

from eye_detector import EyeDetector
from gaze_direction import GazeTracker
from head_movement import HeadPoseEstimator
from calibration import Calibration


class GazeConnect:

    def __init__(self):

        # Open webcam
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            print("Cannot open webcam")
            exit()

        # MediaPipe Face Mesh
        self.mp_face_mesh = mp.solutions.face_mesh

        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )

        # Helper classes
        self.eye_detector = EyeDetector()
        self.gaze_tracker = GazeTracker()
        self.head_pose = HeadPoseEstimator()
        self.calibration = Calibration()

        self.direction = "CENTER"

    def run(self):

        while True:

            success, frame = self.cap.read()

            if not success:
                continue

            frame = cv2.flip(frame, 1)

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = self.face_mesh.process(rgb)

            if results.multi_face_landmarks:

                landmarks = results.multi_face_landmarks[0]

                h, w, _ = frame.shape

                # Detect eyes
                eyes = self.eye_detector.detect(
                    landmarks,
                    w,
                    h
                )

                # Estimate head pose
                pitch, yaw, roll = self.head_pose.estimate(
                    landmarks,
                    w,
                    h
                )

                # Calibrate
                self.calibration.update(
                    eyes,
                    pitch,
                    yaw
                )

                # Estimate gaze
                self.direction = self.gaze_tracker.predict(
                    eyes,
                    pitch,
                    yaw,
                    self.calibration
                )

                # Draw landmarks
                self.eye_detector.draw(
                    frame,
                    eyes
                )

                cv2.putText(
                    frame,
                    f"Direction : {self.direction}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Pitch : {pitch:.1f}",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Yaw : {yaw:.1f}",
                    (20, 110),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 0),
                    2
                )

            cv2.imshow("GazeConnect", frame)

            key = cv2.waitKey(1)

            if key == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":

    app = GazeConnect()
    app.run()