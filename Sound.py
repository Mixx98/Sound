import matplotlib.pyplot as plt
import librosa.display, librosa
import numpy as np

def get_stft(sample_sounds):
    return librosa.stft(sample_sounds)

def get_chroma(sample_sounds, sr):
    return librosa.feature.chroma_stft(S=np.abs(get_stft(sample_sounds)), 
                                       sr=sr)

def draw_chroma(sample_sounds, sr):
    plt.figure(figsize=(12,6))
    librosa.display.specshow(get_chroma(sample_sounds, sr), 
                             y_axis='chroma', x_axis='time')
    plt.grid(); plt.show()

piano, sr=librosa.core.load('piano.wav')
draw_chroma(piano,sr)