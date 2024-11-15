from adafruit_circuitplayground import cp

import time

import random


def Counter():
    count = 1
    while True:
       if cp.button_a:
          count = count + 1
          for i in range(count):
           cp.pixels[i] = (100, 100, 100)
          time.sleep(.200)
            
       elif cp.button_b:
          count = count - 1
          cp.pixels.fill((0,0,0))
          for i in range(count):
           cp.pixels[i] = (100, 100, 100)
          time.sleep(.200)
