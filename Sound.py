import librosa.display, librosa
import IPython.display
import warnings
import numpy as np
import matplotlib.pyplot as plt

warnings.simplefilter("ignore")

def sin_wave(amp, freq, time):
    return amp * np.sin(2*np.pi*freq*time)

sr = 22*1000.
ts = 1/sr

time = np.arange(0, 1, ts)
DO = sin_wave(1, 261.6256, time)
MI = sin_wave(1, 329.6276, time)
SOL = sin_wave(1, 391.9954, time)

plt.figure(figsize=(12,5))
plt.plot(time, DO, label="DO", color='red')
plt.plot(time, MI, label="MI", color='blue')
plt.plot(time, SOL, label="SOL", color='green')
plt.xlim((0, 0.01))
plt.legend(); plt.grid(); plt.show()