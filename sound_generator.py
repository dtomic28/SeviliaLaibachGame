

from pydub import AudioSegment
from pydub.playback import play
  

wav_file = AudioSegment.from_file(file = "file.wav", format = "wav") 
  
# Play the audio file
play(wav_file)

""""
print(f"Channels: {audio_segment.channels}")
print(f"Sample width: {audio_segment.sample_width}")
print(f"Frame rate (sample rate): {audio_segment.frame_rate}")
print(f"Frame width: {audio_segment.frame_width}")
print(f"Length (ms): {len(audio_segment)}")
print(f"Frame count: {audio_segment.frame_count()}")
print(f"Intensity: {audio_segment.dBFS}")
"""