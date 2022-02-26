#imports
import time, machine, neopixel, gc

#define important bits
pin = 1
led_num = 37 - 3
pause = .05
#setup
np = neopixel.NeoPixel(machine.Pin(pin), led_num)

for i in range(led_num):
    np[i] = (0,0,0)
    np.write()
time.sleep(1)

while True:
    for i in range(led_num):
        for j in range(i,led_num):
            np[j] = (50,0,0)       
                
        for j in range(i + 1):
            np[j] = (0,50,0)

        np.write()
        time.sleep(pause)
        
        
    for i in range(led_num,0,-1):
        for j in range(i):
            np[j] = (0,50,0)            #receeding color
        for j in range(i - 1,led_num):
            np[j] = (50,0,0)
        np.write()
        time.sleep(pause)
        gc.collect()
        