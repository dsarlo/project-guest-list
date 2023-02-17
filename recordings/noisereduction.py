import wave, os, glob
from scipy.io import wavfile
import noisereduce as nr
zero = []
path = ''
for filename in glob.glob(os.path.join(path, '*.wav')):
    # load data
    print(filename)
    rate, data = wavfile.read(filename)
    # perform noise reduction
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    wavfile.write(filename + "_reduced_noise.wav", rate, reduced_noise)
    wavfile.close()