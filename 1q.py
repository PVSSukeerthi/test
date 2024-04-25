import numpy as np
import matplotlib.pyplot as plt
import csv

amplitude = float(input("Enter the amplitude of square wave:"))
samples_per_second = int(input("Enter the number of samples per second:"))
frequency = float(input("Enter the frequency:"))
duration = float(input("Enter the duration of the signal:"))
filename = input("Enter the filename for CSV:")

def square_wave(samples_per_second, duration, frequency, amplitude):
    time = np.linspace(0, duration, int(samples_per_second * duration))
    wave = amplitude * np.sign(np.sin(2 * np.pi * frequency * time))
    return time, wave

def save_csv(time, amplitude, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'Amplitude'])
        for t, amp in zip(time, amplitude):
            writer.writerow([t, amp])


t, signal = square_wave(samples_per_second, duration, frequency, amplitude)
plt.plot(t, signal)
plt.xlabel('time (seconds)')
plt.ylabel('Amplitude')   
plt.show()

filename = f"square_wave.csv"
save_csv(t, signal, filename)
