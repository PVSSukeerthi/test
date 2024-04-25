
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

fc = 30
fs = 10
duration = 1
bit_width = 50

t = np.linspace(0, duration, int(fs * duration * bit_width))

def generate_binary_signal(fs, duration):
    #generating random signal and making it into a binary signal
    signal = []
    for i in range(fs * duration):
        signal.append(np.random.randint(0, 2))
    binary_signal = [ele for ele in signal for i in range(bit_width)]
    return binary_signal

def OOK_modulation(fc, t, binary_signal):
    #modulating the signal by multiplying with a carrier sin signal
    carrier = np.sin(2 * np.pi * fc * t)
    modulated_signal = carrier * binary_signal
    return modulated_signal

def OOK_demodulation(modulated_signal, cutoff_freq, fs):
    # To recover the signal using low pass filter and then envolope detection
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_freq / nyquist
    b, a = butter(1, normal_cutoff, btype='low', analog=False)
    envelope = filtfilt(b, a, np.abs(modulated_signal))
    threshold = 0.5  
    demodulated_signal = (envelope > threshold).astype(int)
    
    return demodulated_signal

# Generating binary signal and modulating it
binary_signal = generate_binary_signal(fs, duration)
modulated_signal = OOK_modulation(fc, t, binary_signal)

# Demodulating the modulated signal
cutoff_freq = 0.5 
demodulated_signal = OOK_demodulation(modulated_signal, cutoff_freq, fs)

plt.subplot(3, 1, 1)
plt.plot(t, binary_signal)
plt.title('Binary Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, modulated_signal)
plt.title('Modulated Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t, demodulated_signal)
plt.title('Demodulated Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()