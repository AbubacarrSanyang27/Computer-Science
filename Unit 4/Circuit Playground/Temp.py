from adafruit_circuitplayground import cp



def Temp():
   while True:
      if cp.temperature < 78:
        for i in range(1):
           cp.pixels[i] = (0, 0, 255)

      elif cp.temperature > 78 :
         for i in range(2):
           cp.pixels[i] =(0, 0, 255)

      elif cp.temperature > 79 :
         for i in range(3):
           cp.pixels[i] =(0, 0, 255)

      elif cp.temperature > 80 :
        for i in range(4):
           cp.pixels[i] =(255, 255, 0)

      elif cp.temperature > 81 :
         for i in range(5):
           cp.pixels[i] =(255, 255, 0)
      
      elif cp.temperature > 82 :
         for i in range(6):
           cp.pixels[i] =(255, 255, 0)

      elif cp.temperature > 83 :
         for i in range(7):
           cp.pixels[i] =(255, 255, 0)

      elif cp.temperature > 84 :
         for i in range(8):
           cp.pixels[i] =(255, 0, 0)

      elif cp.temperature > 85 :
         for i in range(9):
           cp.pixels[i] =(255, 0, 0)

      elif cp.temperature > 86 :
         for i in range(10):
           cp.pixels[i] =(255, 0, 0)