from pydub import AudioSegment
from pydub.playback import play

def playPreamble(): 
  # "Hello, please leave a message after the tone"
  song = AudioSegment.from_file('/home/pi/project-guest-list/plamatf.wav')
  play(song)