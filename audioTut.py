import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

fs=44100
duration = 5  # seconds
myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')

print ("Recording Audio")
sd.wait()

print(type(myrecording))
print(myrecording)
# import speech_recognition as sr
# r = sr.Recognizer()
# harvard = sr.AudioFile(myrecording)
# with harvard as source:
#     audio = r.record(source)
# r.recognize_google(audio)

#https://realpython.com/python-speech-recognition/spea
#https://github.com/googleapis/python-speech/blob/master/samples/microphone/transcribe_streaming_infinite.py
print ("Audio recording complete , Play Audio")
sd.play(myrecording, fs)
sd.wait()
print ("Play Audio Complete")
