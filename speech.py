from gtts import gTTS
import pygame
import uuid
import os
import time

mixer_ready = False


def init_audio():
    global mixer_ready

    if mixer_ready:
        return True

    try:
        pygame.mixer.init()
        mixer_ready = True
        return True

    except Exception as e:
        print("Audio unavailable:", e)
        return False


def speak(text):

    if not init_audio():
        print("Speech:", text)
        return

    filename = f"{uuid.uuid4()}.mp3"

    try:

        tts = gTTS(text=text, lang="en")
        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.unload()

    finally:

        if os.path.exists(filename):
            try:
                os.remove(filename)
            except:
                pass