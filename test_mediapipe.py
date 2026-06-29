import mediapipe as mp

print("Version:", mp.__version__)

try:
    print(mp.solutions.face_mesh)
    print("FaceMesh Available ✅")
except Exception as e:
    print("Error:", e)