import cv2
import mediapipe as mp
import time

mp_face_mesh = mp.solutions.face_mesh

gesture_history = []
last_direction = ""

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

            # Calibration for first 3 seconds
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

                cv2.circle(
                    frame,
                    (neutral_x, neutral_y),
                    6,
                    (255, 0, 255),
                    -1
                )

                current_direction = ""

                if x < neutral_x - 40:
                    current_direction = "LEFT"

                elif x > neutral_x + 40:
                    current_direction = "RIGHT"

                elif y < neutral_y - 25:
                    current_direction = "UP"

                elif y > neutral_y + 35:
                    current_direction = "DOWN"

                if current_direction:

                    cv2.putText(
                        frame,
                        current_direction,
                        (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 255, 0),
                        3
                    )

                    if current_direction != last_direction:

                        gesture_history.append(current_direction)
                        last_direction = current_direction

                        if len(gesture_history) > 10:
                            gesture_history.pop(0)

                # YES = UP DOWN UP

                if len(gesture_history) >= 3:

                    if gesture_history[-3:] == ["UP", "DOWN", "UP"]:

                        cv2.putText(
                            frame,
                            "YES DETECTED",
                            (20, 160),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 255, 0),
                            3
                        )

                    # NO = LEFT RIGHT LEFT

                    if gesture_history[-3:] == ["LEFT", "RIGHT", "LEFT"]:

                        cv2.putText(
                            frame,
                            "NO DETECTED",
                            (20, 160),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 0, 255),
                            3
                        )

                cv2.putText(
                    frame,
                    f"History: {gesture_history[-5:]}",
                    (20, 220),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    2
                )

        cv2.imshow("GazeConnect Head Gesture System", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()