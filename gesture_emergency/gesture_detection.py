import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True
) as face_mesh:

    while True:
        success, frame = cap.read()

        if not success:
            break

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
                1,
                (0, 255, 0),
                2
            )

        cv2.imshow("Head Tracking", frame)

        if cv2.waitKey(1) == 27:
            break

cap.release()
cv2.destroyAllWindows()