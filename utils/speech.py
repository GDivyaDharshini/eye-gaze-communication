import pyttsx3

# -----------------------------------------
# Initialize Speech Engine (Only Once)
# -----------------------------------------

engine = pyttsx3.init()

engine.setProperty("rate", 150)      # Speech Speed
engine.setProperty("volume", 1.0)    # Maximum Volume


# -----------------------------------------
# Speak Function
# -----------------------------------------

def speak(text):

    try:

        if not text:
            return

        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print("Speech Error:", e)