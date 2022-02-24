import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf
import pyloudnorm as pyln

s_rate, signal = wavfile.read(r"C:\Users\majar\Documents\GitHub\SeviliaLaibachGame\testSound.py\test.wav")
FFT = signal
freqs=fftpk.fftfreq(len(FFT),(1.0/s_rate))
st=0
timer=0
min=0
max=10000000

with open("datoteka.txt","w") as f:
    for i in range(0,len(signal),s_rate//10):
        print(str(signal[i])+" "+str(timer)+": s")
        st=(st+1)%10
        if(st==9):
            timer+=1
        f.write(str(signal[i]))


data, rate = sf.read(r"C:\Users\majar\Documents\GitHub\SeviliaLaibachGame\testSound.py\test.wav")
meter = pyln.Meter(rate) 
print(data[10000][0])
"""
for i in range(0,len(data),):
    loudness = meter.integrated_loudness(data[i])
    print(loudness)

"""
plt.plot(freqs[range(len(FFT))],FFT[range(len(FFT))])
plt.xlabel("frequency (Hz)")
plt.ylabel("Amplitude")
plt.show()