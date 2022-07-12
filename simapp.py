import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import random

class App:
    def __init__(self):
        st.title("ADC simulation")
        t, wave, freq, amp = self.signal()
        self.graph(t, wave, freq, amp)
        
    
    def signal(self):
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
        freq = np.linspace(0, 1/dt, N)
        amp = np.abs(f) * (2 / N)       
        
        return t, wave, freq, amp 
        
    def graph(self, t, wave, freq, amp):
        fig = plt.figure(figsize=(16,9))
        
        ax1 = fig.add_subplot(2,1,1)
        ax1.plot(t, wave, label="signal")
        ax1.set_xlabel("time[s]")
        ax1.set_ylabel("voltage[V]")
        ax1.grid()
        ax1.legend()
        
        ax2 = fig.add_subplot(2,1,2)
        ax2.set_yscale("log")
        ax2.bar(freq, amp, label="amplitude")
        ax2.set_xlabel("frequency[Hz]")
        ax2.set_ylabel("amplitude[V]")
        ax2.grid()
        ax2.legend()
        ax2.set_xlim(0,100)
        
        st.pyplot(fig)
        
if __name__ == "__main__":
    App()