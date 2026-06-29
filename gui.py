import tkinter as tk
from tkinter import ttk
from gtts import gTTS
import pygame
import json
import uuid
import time
import os

# -------------------------
# Initialize Pygame
# -------------------------
pygame.mixer.init()

# -------------------------
# Load Language File
# -------------------------
def load_language(language):
    files = {
        "English": "english.json",
        "Hindi": "hindi.json",
        "Tamil": "tamil.json",
        "Bengali": "bengali.json"
    }

    with open(files[language], "r", encoding="utf-8") as file:
        return json.load(file)

# -------------------------
# Speak Function
# -------------------------
def speak(text, language):

    lang_codes = {
        "English": "en",
        "Hindi": "hi",
        "Tamil": "ta",
        "Bengali": "bn"
    }

    filename = f"{uuid.uuid4()}.mp3"

    try:
        tts = gTTS(
            text=text,
            lang=lang_codes[language]
        )

        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            root.update()
            time.sleep(0.1)

        pygame.mixer.music.unload()

    except Exception as e:
        print("Speech Error:", e)

    finally:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except:
                pass

# -------------------------
# Speak Phrase
# -------------------------
def speak_phrase(phrase):

    language = language_var.get()

    phrases = load_language(language)

    if phrase in phrases:

        text = phrases[phrase]

        status_label.config(
            text=f"Speaking: {text}"
        )

        speak(text, language)

# -------------------------
# Main Window
# -------------------------
root = tk.Tk()

root.title("Eye Gaze Communication System")
root.geometry("900x700")
root.configure(bg="#EAF4FF")

# -------------------------
# Title
# -------------------------
title = tk.Label(
    root,
    text="Eye Gaze Communication System",
    font=("Arial", 22, "bold"),
    bg="#EAF4FF"
)

title.pack(pady=15)

# -------------------------
# Language Selection
# -------------------------
language_var = tk.StringVar(value="English")

tk.Label(
    root,
    text="Select Language",
    font=("Arial", 12, "bold"),
    bg="#EAF4FF"
).pack()

language_menu = ttk.Combobox(
    root,
    textvariable=language_var,
    values=[
        "English",
        "Hindi",
        "Tamil",
        "Bengali"
    ],
    state="readonly",
    width=20
)

language_menu.pack(pady=10)

# -------------------------
# BASIC NEEDS
# -------------------------
basic_frame = tk.LabelFrame(
    root,
    text="Basic Needs",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10
)

basic_frame.pack(padx=10, pady=10, fill="x")

basic_phrases = [
    "hello",
    "water",
    "food",
    "washroom",
    "thankyou"
]

for phrase in basic_phrases:

    btn = tk.Button(
        basic_frame,
        text=phrase.capitalize(),
        width=18,
        height=2,
        command=lambda p=phrase: speak_phrase(p)
    )

    btn.pack(side="left", padx=5, pady=5)

# -------------------------
# MEDICAL
# -------------------------
medical_frame = tk.LabelFrame(
    root,
    text="Medical",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10
)

medical_frame.pack(padx=10, pady=10, fill="x")

medical_phrases = [
    "pain",
    "medicine",
    "doctor"
]

for phrase in medical_phrases:

    btn = tk.Button(
        medical_frame,
        text=phrase.capitalize(),
        width=18,
        height=2,
        command=lambda p=phrase: speak_phrase(p)
    )

    btn.pack(side="left", padx=5, pady=5)

# -------------------------
# COMMUNICATION
# -------------------------
comm_frame = tk.LabelFrame(
    root,
    text="Communication",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10
)

comm_frame.pack(padx=10, pady=10, fill="x")

comm_phrases = [
    "yes",
    "no",
    "family",
    "help"
]

for phrase in comm_phrases:

    btn = tk.Button(
        comm_frame,
        text=phrase.capitalize(),
        width=18,
        height=2,
        command=lambda p=phrase: speak_phrase(p)
    )

    btn.pack(side="left", padx=5, pady=5)

# -------------------------
# EMERGENCY
# -------------------------
emergency_frame = tk.LabelFrame(
    root,
    text="Emergency",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10
)

emergency_frame.pack(padx=10, pady=10, fill="x")

emergency_btn = tk.Button(
    emergency_frame,
    text="EMERGENCY",
    bg="red",
    fg="white",
    font=("Arial", 14, "bold"),
    width=25,
    height=2,
    command=lambda: speak_phrase("emergency")
)

emergency_btn.pack(pady=10)

# -------------------------
# Status Label
# -------------------------
status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 12, "bold"),
    fg="blue",
    bg="#EAF4FF"
)

status_label.pack(pady=15)

root.mainloop()