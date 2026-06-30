import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def get_frame(self):
        success, frame = self.cap.read()

        if success:
            return frame

        return None

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()