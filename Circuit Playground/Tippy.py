from adafruit_circuitplayground import cp



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