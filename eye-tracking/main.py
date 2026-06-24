import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True
)

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    direction = "CENTER"

    if results.multi_face_landmarks:

        h, w, _ = frame.shape

        for face_landmarks in results.multi_face_landmarks:

            # Left eye corners
            left_corner = face_landmarks.landmark[33]
            right_corner = face_landmarks.landmark[133]

            # Iris center
            iris = face_landmarks.landmark[468]

            # Convert to pixel coordinates
            lx = int(left_corner.x * w)
            rx = int(right_corner.x * w)
            ix = int(iris.x * w)

            ly = int(left_corner.y * h)
            ry = int(right_corner.y * h)
            iy = int(iris.y * h)

            # Draw points
            cv2.circle(frame, (lx, ly), 3, (255, 0, 0), -1)
            cv2.circle(frame, (rx, ry), 3, (255, 0, 0), -1)
            cv2.circle(frame, (ix, iy), 5, (0, 255, 0), -1)

            # Eye width
            eye_width = rx - lx

            if eye_width > 0:

                horizontal_ratio = (ix - lx) / eye_width

                if horizontal_ratio < 0.35:
                    direction = "LEFT"

                elif horizontal_ratio > 0.65:
                    direction = "RIGHT"

                else:
                    direction = "CENTER"

    cv2.putText(
        frame,
        f"Direction: {direction}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow("GazeConnect Eye Tracking", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()