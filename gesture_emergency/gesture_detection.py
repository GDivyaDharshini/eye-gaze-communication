import cv2
import mediapipe as mp
import time

mp_face_mesh = mp.solutions.face_mesh

cap = cv2.VideoCapture(0)

neutral_x = None
neutral_y = None

start_time = time.time()

with mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:

    while True:
        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:

            face_landmarks = results.multi_face_landmarks[0]

            nose = face_landmarks.landmark[1]

            h, w, _ = frame.shape

            x = int(nose.x * w)
            y = int(nose.y * h)

            cv2.circle(frame, (x, y), 8, (0, 255, 0), -1)

            cv2.putText(
                frame,
                f"X:{x} Y:{y}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

            # Calibrate for first 3 seconds
            if time.time() - start_time < 3:

                neutral_x = x
                neutral_y = y

                cv2.putText(
                    frame,
                    "LOOK STRAIGHT - CALIBRATING",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2
                )

            else:

                cv2.circle(frame, (neutral_x, neutral_y),
                           6, (255, 0, 255), -1)

                if x < neutral_x - 40:
                    cv2.putText(
                        frame,
                        "LEFT",
                        (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 0, 0),
                        3
                    )

                elif x > neutral_x + 40:
                    cv2.putText(
                        frame,
                        "RIGHT",
                        (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 0, 0),
                        3
                    )

                if y < neutral_y - 30:
                    cv2.putText(
                        frame,
                        "UP",
                        (20, 120),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 255),
                        3
                    )

                elif y > neutral_y + 30:
                    cv2.putText(
                        frame,
                        "DOWN",
                        (20, 120),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 255),
                        3
                    )

        cv2.imshow("GazeConnect Head Tracking", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()