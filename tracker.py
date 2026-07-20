import cv2

camera = cv2.VideoCapture(0)

def get_frame():
    success, frame = camera.read()

    if not success:
        return None

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    return frame