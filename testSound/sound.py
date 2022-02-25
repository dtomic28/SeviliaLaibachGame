from pygame_menu import Sound
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf
import pyloudnorm as pyln
def soundCheck():
    s_rate, signal = wavfile.read(r"C:\Users\majar\Documents\GitHub\SeviliaLaibachGame\testSound\file.wav")
    FFT = signal
    freqs=fftpk.fftfreq(len(FFT),(1.0/s_rate))
    st=0
    timer=0
    min=0
    max=0
    SoundWaveSez=[]
    for i in range(0,len(signal),s_rate//10):
        if(int(signal[i])>max):
            max=int(signal[i])
        if(int(signal[i])<min):
            min = int(signal[i])
        st=(st+1)%10
        if(st==9):
            timer+=1
        SoundWaveSez.append(int(signal[i]))

    SpawnObject=[]
    for i in SoundWaveSez:
        SpawnObject.append(((i+abs(min))/(max+abs(min))*5)//1)
    return(SpawnObject)

if __name__ == "main":
    soundCheck()