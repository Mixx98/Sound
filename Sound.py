import matplotlib.pyplot as plt
import librosa.display, librosa
import numpy as np
from IPython.display import Audio

def get_stft(sample_sounds):
    return librosa.stft(sample_sounds)

def get_chroma(sample_sounds, sr):
    return librosa.feature.chroma_stft(S=np.abs(get_stft(sample_sounds)), sr=sr)

def draw_chroma(sample_sounds, sr):
    plt.figure(figsize=(12,6))
    librosa.display.specshow(get_chroma(sample_sounds, sr), y_axis='chroma', x_axis='time')
    plt.grid()

def sin_wave(amp, freq, time):
    return amp * np.sin(2*np.pi*freq*time)

sr = 22*1000.
ts = 1/sr
ts2 = 2/sr

time = np.arange(0, 1, ts)
time2 = np.arange(0, 1, ts2)

DO = sin_wave(1, 261.6256, time)
DO2 = sin_wave(1, 261.6256, time2)
MI = sin_wave(1, 329.6276, time)
SOL = sin_wave(1, 391.9954, time)

toy, sr = librosa.core.load('C:/Users/Hyunsue/Downloads/toy.wav')
self, sr = librosa.core.load('C:/Users/Hyunsue/Downloads/self.wav')

print(DO.size)
print(self.size)
draw_chroma(self-toy,sr)
#draw_chroma(DO+MI,sr)
#sub=DO-DO
#draw_chroma(sub,sr)
#plt.show()