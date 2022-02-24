import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt
<<<<<<< Updated upstream
import pydub

=======
from pydub import AudioSegment
from pydub.playback import play
  

wav_file = AudioSegment.from_file(file = "file.wav", format = "wav") 
>>>>>>> Stashed changes

s_rate, signal = wavfile.read(r"C:\Users\majar\Documents\GitHub\SeviliaLaibachGame\testSound.py\file.wav")
FFT = signal
freqs=fftpk.fftfreq(len(FFT),(1.0/s_rate))
st=0
with open("datoteka.txt","w") as f:
    for i in range(0,len(signal),8000):
        st+=1
        print(signal[i])
        f.write(str(signal[i]))
print(st)
plt.plot(freqs[range(len(FFT))],FFT[range(len(FFT))])
plt.xlabel("frequency (Hz)")
plt.ylabel("Amplitude")
plt.show()