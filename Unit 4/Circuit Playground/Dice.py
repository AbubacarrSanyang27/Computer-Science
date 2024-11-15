from adafruit_circuitplayground import cp

import random


def Dice():
    while True:
     if cp.button_a:
         roll = (random.randint(-1,5))
         for i in range(roll):
            cp.pixels[i] = (0, 0, 100)
     elif cp.button_b:
         cp.pixels.fill((0, 0, 0))

Dice()
