from gtts import gTTS
import pygame
import uuid
import os
import time

pygame.mixer.init()


def speak(text):

    filename = f"{uuid.uuid4()}.mp3"

    try:

        tts = gTTS(
            text=text,
            lang="en"
        )

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