import RPi.GPIO as GPIO
import motorControl
from time import sleep
from msvcrt import getch

GPIO.setmode(GPIO.BOARD)
m1 = Motor([18,22,24,26])
m2 = MOtor([15,19,23,23])
m1.rpm = 15
m2.rpm = 15

pos = {'m1':0,'m2':0}
try:
    while True:
        cmd = getch()
        if cmd == 'w':
            pos['m1']+=1
            m1.move(pos['m1'])
        if cmd == 's':
            pos['m1']-=1
            m1.move(pos['m1'])

        if cmd == 'a':
            pos['m2']+=1
            m1.move(pos['m2'])
        if cmd == 'd':
            pos['m2']-=1
            m1.move(pos['m2'])
except KeyboardInterrupt:
    GPIO.cleanup()