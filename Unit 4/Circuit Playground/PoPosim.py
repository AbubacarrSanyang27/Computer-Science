from adafruit_circuitplayground import cp

import time


def PoPoSim():
    while True:
     cp.pixels.fill((255, 0, 0 ))
     cp.play_tone(500, 0.5)
     cp.pixels.fill((0, 0, 255))
     cp.play_tone(900, 0.5)