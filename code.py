from adafruit_circuitplayground.express import cpx
import time

turquoise = (34, 100, 100) 
yellow = (40, 40, 0)
blueval = 200
pink = (120, 70, 70)
off = (0, 0, 0)

# Tap twice to toggle
cpx.detect_taps = 1
while True:
    if cpx.tapped:
        print("Tapped!")
        cpx.pixels.fill (pink)
    time.sleep(0.5)
    
    
    
while True:
    for i in range(0, 10):
        cpx.pixels[i] = yellow
    print (i) 
    time.sleep(0.1)
    
    if cpx.switch:
        cpx.pixels[3] =  yellow
    else:
        cpx.pixels.fill(off)
    
while True: 
    cpx.pixels.fill((0, 0, blueval))
    print (blueval)
    blueval = blueval - 5
    time.sleep(0.01)