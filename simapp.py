import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import random

class App:
    def __init__(self):
        st.title("ADC simulation")
        self.side()
        t, wave, freq, amp = self.signal()
        self.graph(t, wave, freq, amp)
            
    def signal(self):

        t = np.arange(0, self.N * self.dt, self.dt) # 時間 [s]
        x = 100 * np.sin(2*np.pi*self.f*t)
        wave = [i + random.uniform(-1*self.r, self.r) for i in x]  
        f = np.fft.fft(wave)
        freq = np.linspace(0, 1/self.dt, self.N)
        amp = np.abs(f) * (2 / self.N)       
        
        return t, wave, freq, amp 
    
    def side(self):
        st.sidebar.header("各種変数の設定")

        self.f = st.sidebar.number_input("", 49.0, 51.0, 50.0)
        st.sidebar.write(f"現在の周波数は{self.f} Hzです")
        
        self.N = st.sidebar.number_input("サンプル数", 128, 16384, 1024)
        st.sidebar.write(f"現在のサンプル数は{self.N}点です")
        
        self.dt = st.sidebar.number_input("サンプリング周期", 1.0 * 10 ** (-6), 1.0 * 10 ** (-1), 1.0 * 10 **(-3))
        st.sidebar.write(f"現在のサンプリング周期は{self.dt} sです")
        
        self.lim = st.sidebar.number_input("表示範囲", 100, 1000, 100)
        st.sidebar.write(f"現在の表示範囲は 0<f<{self.lim} です")
        
        self.r = st.sidebar.slider("ランダムなノイズ[V]", min_value=0.0, max_value=10.0, value=0.0)
        
    def graph(self, t, wave, freq, amp):
        fig = plt.figure(figsize=(20,12))
        plt.subplots_adjust(wspace=0, hspace=0.3)
        plt.rcParams["font.size"] = 18
        
        ax1 = fig.add_subplot(2,1,1)
        ax1.plot(t, wave)
        ax1.set_xlabel("time[s]")
        ax1.set_ylabel("voltage[V]")
        ax1.grid()
        # ax1.legend()
        
        ax2 = fig.add_subplot(2,1,2)
        ax2.set_yscale("log")
        ax2.bar(freq, amp)
        ax2.set_xlabel("frequency[Hz]")
        ax2.set_ylabel("amplitude[V]")
        ax2.grid()
        # ax2.legend()
        ax2.set_xlim(0,self.lim)
        
        st.pyplot(fig)
        
if __name__ == "__main__":
    App()