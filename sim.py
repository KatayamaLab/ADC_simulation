import numpy as np
import matplotlib.pyplot as plt
import random
import streamlit as st

N = 8192        # サンプル数
dt = 0.0001          # サンプリング周期 [s]
f1 = 50    # 周波数 [Hz]

t = np.arange(0, N*dt, dt) # 時間 [s]
x = 100 * np.sin(2*np.pi*f1*t)
wave = []

for i in range(len(x)):
    tmp = x[i] + random.uniform(-0.1,0.1)
    wave.append(tmp)

f = np.fft.fft(wave)
# freq = np.fft.fftfreq(N, d=dt)
freq = np.linspace(0, 1/dt, N)
amp = np.abs(f) * (2 / N)

plt.figure(figsize=(16,9))

plt.subplot(211)
plt.plot(t, wave, label="signal")
plt.xlabel("time[s]")
plt.ylabel("voltage[V]")
plt.grid()
plt.legend()

plt.subplot(212)
plt.yscale("log")
plt.bar(freq, amp, label="amplitude")
plt.xlabel("frequency[Hz]")
plt.ylabel("amplitude[V]")
plt.grid()
plt.legend()
plt.xlim(0,100,10)

plt.show()