import RPi.GPIO as GPIO
import time
import pyaudio
import numpy as np

GPIO.setmode(GPIO.BCM)
def line(num_of_pins):
        arr=[18,23,24,25,12,16,20,21,17,27,22,5,6,13,19,26]
        for i in arr[:num_of_pins]:
                GPIO.setup(i,GPIO.OUT)
                GPIO.output(i,GPIO.HIGH)
                time.sleep(0.005)
                GPIO.output(i,GPIO.LOW)
                time.sleep(0.005)


CHUNK = 2**11
RATE = 44100
p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)
try:
    while True:
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)

        peak=np.average(np.abs(data))*2
        bars="*"*int((50*peak/2**16)*2)
        print(bars)
        line(bars)
except:
    stream.stop_stream()
    stream.close()
    p.terminate()
