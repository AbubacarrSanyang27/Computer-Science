from adafruit_circuitplayground import cp

import time

import random


def Meter():
  while True:
      if cp.light > 30:
        for i in range(1):
           cp.pixels[i] = (0, 0, 10)

      elif cp.light > 27:
         for i in range(2):
           cp.pixels[i] =(0, 0, 10)

      elif cp.light > 24:
         for i in range(3):
           cp.pixels[i] =(0, 0, 10)
      elif cp.light > 21:         
        for i in range(4):
           cp.pixels[i] =(0, 0, 10)

      elif cp.light > 18:         
         for i in range(5):
           cp.pixels[i] =(0, 0, 10)
      
      elif cp.light > 15:          
         for i in range(6):
           cp.pixels[i] =(0, 0, 10)

      elif cp.light > 12:         
         for i in range(7):
           cp.pixels[i] =(0, 0, 10)

      elif cp.light > 9:         
         for i in range(8):
           cp.pixels[i] =(0, 0, 10)

      elif cp.light > 6:         
         for i in range(9):
           cp.pixels[i] =(0, 0, 10)

      elif cp.light > 3:        
         for i in range(10):
           cp.pixels[i] =(0, 0, 10)

Meter()