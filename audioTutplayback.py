import sounddevice as sd
duration = 100  # seconds

import speech_recognition as sr
r = sr.Recognizer()

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    r.recognize_google(indata)
    outdata[:] = indata

with sd.Stream(channels=2, callback=callback):
    sd.sleep(int(duration * 1000))


