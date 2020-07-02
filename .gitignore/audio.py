import math        #import needed modules
import pyaudio     # for linux sudo apt-get install python-pyaudio and for window pip install pyaudio

PyAudio = pyaudio.PyAudio     #initialize pyaudio

#See https://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 20000     #number of frames per second/frameset.      

FREQUENCY = 500     #Hz, waves per second, 261.63=C4-note.
LENGTH = 3     #seconds to play sound

if FREQUENCY > BITRATE:
    BITRATE = FREQUENCY+100ss

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''    

#generating wawes
for x in range(NUMBEROFFRAMES):
 WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

for x in range(RESTFRAMES): 
 WAVEDATA = WAVEDATA+chr(128)

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = BITRATE, 
                output = True)

stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()
