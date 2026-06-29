import cv2
import json
import time

from camera_test import Camera
from eye_tracking import EyeTracker
from speech import speak


# -------------------------
# Languages
# -------------------------

languages = [
    "english",
    "tamil",
    "hindi",
    "bengali"
]

language_index = 0
selected_language = languages[0]

language_mode = True


# -------------------------
# Camera & Tracking
# -------------------------

camera = Camera()
tracker = EyeTracker()


# -------------------------
# Phrase Data
# -------------------------

phrases = {}
phrase_names = []
current_index = 0


# -------------------------
# Movement Delay
# -------------------------

MOVE_DELAY = 1.0
last_move = time.time()


# -------------------------
# Blink Variables
# -------------------------

blink_count = 0
last_blink_time = 0

DOUBLE_BLINK_WINDOW = 1.0
BLINK_DECISION_DELAY = 1.2

blink_active = False

confirm_action = False
emergency_action = False

CONFIRM_COOLDOWN = 3
last_confirm_time = 0


print("\nEye Gaze Communication Started")
print("Double Blink = Confirm / Speak")
print("Triple Blink = Emergency Alert")
print("Q = Quit\n")


while True:

    frame = camera.get_frame()

    if frame is None:
        continue

    direction, blink = tracker.detect(frame)

    current_time = time.time()

    # -------------------------
    # Blink Detection
    # -------------------------

    confirm_action = False
    emergency_action = False

    if (
        current_time - last_confirm_time
        > CONFIRM_COOLDOWN
    ):

        if blink and not blink_active:

            blink_active = True

            if (
                current_time - last_blink_time
                < DOUBLE_BLINK_WINDOW
            ):
                blink_count += 1

            else:
                blink_count = 1

            last_blink_time = current_time

        elif not blink:
            blink_active = False

        if (
            blink_count > 0
            and current_time - last_blink_time
            > BLINK_DECISION_DELAY
        ):

            if blink_count == 2:
                confirm_action = True

            elif blink_count >= 3:
                emergency_action = True

            blink_count = 0

    # =========================
    # LANGUAGE MODE
    # =========================

    if language_mode:

        if (
            current_time - last_move
            > MOVE_DELAY
        ):

            if direction == "UP":

                language_index = (
                    language_index - 1
                ) % len(languages)

                last_move = current_time

            elif direction == "DOWN":

                language_index = (
                    language_index + 1
                ) % len(languages)

                last_move = current_time

            elif direction == "LEFT":

                language_index = (
                    language_index - 1
                ) % len(languages)

                last_move = current_time

            elif direction == "RIGHT":

                language_index = (
                    language_index + 1
                ) % len(languages)

                last_move = current_time

        selected_language = (
            languages[language_index]
        )

        cv2.putText(
            frame,
            "LANGUAGE SELECTION",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            selected_language.upper(),
            (20, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            "DOUBLE BLINK TO CONFIRM",
            (20, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

        if confirm_action:

            with open(
                f"language/{selected_language}.json",
                "r",
                encoding="utf-8"
            ) as file:

                phrases = json.load(file)

            phrase_names = list(
                phrases.keys()
            )

            current_index = 0

            language_mode = False

            print(
                f"Language Selected: "
                f"{selected_language}"
            )

            last_confirm_time = time.time()

    # =========================
    # PHRASE MODE
    # =========================

    else:

        if (
            current_time - last_move
            > MOVE_DELAY
        ):

            if direction == "RIGHT":

                current_index = (
                    current_index + 1
                ) % len(phrase_names)

                last_move = current_time

            elif direction == "LEFT":

                current_index = (
                    current_index - 1
                ) % len(phrase_names)

                last_move = current_time

        selected_phrase = (
            phrase_names[current_index]
        )

        cv2.putText(
            frame,
            f"Direction: {direction}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Phrase: {selected_phrase}",
            (20, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            "DOUBLE BLINK TO SPEAK",
            (20, 140),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

        cv2.putText(
            frame,
            "TRIPLE BLINK = EMERGENCY",
            (20, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

        if confirm_action:

            text = phrases[selected_phrase]

            print("Speaking:", text)

            speak(text)

            last_confirm_time = time.time()

        elif emergency_action:

            emergency_text = (
                "Emergency! Please help me immediately!"
            )

            print("EMERGENCY ALERT")

            speak(emergency_text)

            last_confirm_time = time.time()

    # -------------------------
    # Status
    # -------------------------

    cv2.putText(
        frame,
        f"Blink Count: {blink_count}",
        (20, 230),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    cv2.imshow(
        "Eye Gaze Communication System",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

    try:

        if cv2.getWindowProperty(
            "Eye Gaze Communication System",
            cv2.WND_PROP_VISIBLE
        ) < 1:
            break

    except:
        break


camera.release()

print("\nProgram Closed")