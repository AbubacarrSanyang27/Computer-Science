from adafruit_circuitplayground import cp

import time






def Woosh():
 while True:
     if cp.button_a:
      cp.pixels[0] = (100, 0, 0) 
      time.sleep(0.100)
      cp.pixels[0] = (0, 0, 0)  
      cp.pixels[1] = (0, 100, 0)
      time.sleep(0.100) 
      cp.pixels[1] = (0, 0, 0)
      cp.pixels[2] = (0, 0, 100)
      time.sleep(0.100)
      cp.pixels[2] = (0, 0, 0)
      cp.pixels[3] = (100, 100, 0)
      time.sleep(0.100)
      cp.pixels[3] = (0, 0, 0)
      cp.pixels[4] = (100, 0, 100)
      time.sleep(0.100)
      cp.pixels[4] = (0, 0, 0)     
      cp.pixels[5] = (0, 100, 100)
      time.sleep(0.100)
      cp.pixels[5] = (0, 0, 0)   
      cp.pixels[6] = (100, 100, 100) 
      time.sleep(0.100)
      cp.pixels[6] = (0, 0, 0)
      cp.pixels[7] = (0, 100, 100)
      time.sleep(0.100)
      cp.pixels[7] = (0, 0, 0)
      cp.pixels[8] = (100, 0, 100)
      time.sleep(0.100)
      cp.pixels[8] = (0, 0, 0)
      cp.pixels[9] = (100, 100, 0)
      time.sleep(0.100)
      cp.pixels[9] = (0, 0, 0)

     elif cp.button_b:
      cp.pixels[9] = (100, 0, 0) 
      time.sleep(0.100)
      cp.pixels[9] = (0, 0, 0)  
      cp.pixels[8] = (0, 100, 0)
      time.sleep(0.100) 
      cp.pixels[8] = (0, 0, 0)
      cp.pixels[7] = (0, 0, 100)
      time.sleep(0.100)
      cp.pixels[7] = (0, 0, 0)
      cp.pixels[6] = (100, 100, 0)
      time.sleep(0.100)
      cp.pixels[6] = (0, 0, 0)
      cp.pixels[5] = (100, 0, 100)
      time.sleep(0.100)
      cp.pixels[5] = (0, 0, 0)     
      cp.pixels[4] = (0, 100, 100)
      time.sleep(0.100)
      cp.pixels[4] = (0, 0, 0)   
      cp.pixels[3] = (100, 100, 100) 
      time.sleep(0.100)
      cp.pixels[3] = (0, 0, 0)
      cp.pixels[2] = (0, 100, 100)
      time.sleep(0.100)
      cp.pixels[2] = (0, 0, 0)
      cp.pixels[1] = (100, 0, 100)
      time.sleep(0.100)
      cp.pixels[1] = (0, 0, 0)
      cp.pixels[0] = (100, 100, 0)
      time.sleep(0.100)
      cp.pixels[0] = (0, 0, 0) 