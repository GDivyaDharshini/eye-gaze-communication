import winsound
import pyttsx3

engine = pyttsx3.init()

def trigger_emergency():

    print("🚨 EMERGENCY ALERT ACTIVATED 🚨")

    for _ in range(5):
        winsound.PlaySound(
            "SystemExclamation",
            winsound.SND_ALIAS
        )

    engine.say(
        "Emergency. Caregiver assistance required immediately."
    )

    engine.runAndWait()

if __name__ == "__main__":
    trigger_emergency()