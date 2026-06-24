import pyttsx3
import winsound
import time

engine = pyttsx3.init()

def trigger_emergency():

    print("🚨 EMERGENCY ALERT ACTIVATED 🚨")

    for i in range(3):
        winsound.Beep(1000, 500)
        time.sleep(0.2)

    engine.say(
        "Emergency. Caregiver assistance required immediately."
    )

    engine.runAndWait()

if __name__ == "__main__":
    trigger_emergency()