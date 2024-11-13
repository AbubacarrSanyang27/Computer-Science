from adafruit_circuitplayground import cp

import time


def blinky():
   while True:
      cp.pixels.fill((0, 0, 55))
      time.sleep(.367)
      cp.pixels.fill((0, 0, 0))
      time.sleep(.367)
      blinky()



def Flip_Flop():
   while True:
      if cp.switch:
         cp.pixels[0] = (255, 0, 0)   
         cp.pixels[1] = (0, 255, 0) 
         cp.pixels[2] = (0, 0, 255)
         cp.pixels[3] = (0, 225, 255)
         cp.pixels[4] = (225, 0, 255)
         cp.pixels[5] = (0, 0, 0)   
         cp.pixels[6] = (0, 0, 0) 
         cp.pixels[7] = (0, 0, 0)
         cp.pixels[8] = (0, 0, 0)
         cp.pixels[9] = (0, 0, 0)  
         

      else:
         cp.pixels[0] = (0, 0, 0)   
         cp.pixels[1] = (0, 0, 0) 
         cp.pixels[2] = (0, 0, 0)
         cp.pixels[3] = (0, 0, 0)
         cp.pixels[4] = (0, 0, 0)     
         cp.pixels[5] = (255, 0, 0)   
         cp.pixels[6] = (0, 255, 0) 
         cp.pixels[7] = (0, 0, 255)
         cp.pixels[8] = (0, 225, 255)
         cp.pixels[9] = (225, 0, 255)  


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



def Spin():     #Bonus because i was curiuos
 while True:
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

def Tippy():
   while True:
       x, y, z = cp.acceleration
       if x > 3:
         cp.pixels[1] = (0, 255, 0) 
         cp.pixels[2] = (0, 0, 255)
         cp.pixels[3] = (0, 225, 255)
         cp.pixels[6] = (0, 0, 0) 
         cp.pixels[7] = (0, 0, 0)
         cp.pixels[8] = (0, 0, 0)
       elif x < -3:
         cp.pixels[1] = (0, 0, 0) 
         cp.pixels[2] = (0, 0, 0)
         cp.pixels[3] = (0, 0, 0)
         cp.pixels[6] = (0, 255, 0) 
         cp.pixels[7] = (0, 0, 255)
         cp.pixels[8] = (0, 225, 255)

def Temp():
   while True:
      if 78 < cp.temperature < 78:
         cp.pixels.fill(0, 0, 255) 

      if cp.temperature > 79 :
         cp.pixels.fill(0, 0, 0)


      

Temp()
