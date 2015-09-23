

from time import sleep
import RPi.GPIO as GPIO


class Pin(object):
        def __init__(self, number):
                self.num = number
                self.state = False

class Motor(object)
        def __init__(self, pins):
                self.pins = []
                for p in pins:
                        self.pins.append(Pin(p))
                self.steps = 0
                self.deg_per_step = 5.625 / 64  # for half-step drive (mode 3)
                self.steps_per_rev = int(360 / self.deg_per_step)  # 4096

                for p in pins:
                        GPIO.setup(p.num, GPIO.OUT)
                        self.set_pin(p,False)

        def _set_rpm(self, rpm):
                self._rpm = rpm
                self._T = (60.0 / rpm) / self.steps_per_rev # Time between signals

        rpm = property(lambda self: self._rpm, _set_rpm)

        def __clear(self):
                for p in self.pins:
                        self.set_pin(p,False)


        def set_pin(pin, state):
                if state:
                        GPIO.output(pin.num,1)
                        pin.state = True
                else:
                        GPIO.output(pin.num,0)
                        pin.state = False

        def move(self, direc):
                if direc > 0: # move clockwise
                        # P1    0 0 0 0 0 0 1 1 1
                        # P2    0 0 0 0 1 1 1 0 0
                        # P3    0 0 1 1 1 0 0 0 0 
                        # P4    0 1 1 0 0 0 0 0 1
                        if (not(pins[0].state) and not(pins[1].state) and not(pins[2].state) and not(pins[3].state)):
                                # Case 0 0 0 0
                                self.set_pin(pons[3],True)
                        elif (not(pins[0].state) and not(pins[1].state) and not(pins[2].state) and pins[3].state):   
                                # Case 0 0 0 1
                                self.set_pin(pins[2],True)
                        elif (not(pins[0].state) and not(pins[1].state) and (pins[2].state) and (pins[3].state)):
                                # Case 0 0 1 1
                                self.set_pin(pins[3],False)
                        elif (not(pins[0].state) and not(pins[1].state) and (pins[2].state) and not(pins[3].state)):
                                # Case 0 0 1 0 
                                self.set_pin(pins[1],True)
                        elif (not(pins[0].state) and (pins[1].state) and (pins[2].state) and not(pins[3].state)):
                                # Case 0 1 1 0
                                self.set_pin(pins[2],False)
                        elif (not(pins[0].state) and (pins[1].state) and not(pins[2].state) and not(pins[3].state)):
                                # Case 0 1 0 0
                                self.set_pin(pins[0],True)
                        elif ((pins[0].state) and (pins[1].state) and not(pins[2].state) and not(pins[3].state)):
                                # Case 1 1 0 0
                                self.set_pin(pins[1],False)
                        elif ((pins[0].state) and not(pins[1].state) and not(pins[2].state) and not(pins[3].state)):
                                # Case 1 0 0 0 
                                self.set_pin(pins[3],True)
                        elif ((pins[0].state) and not(pins[1].state) and not(pins[2].state) and (pins[3].state)):
                                # Case 1 0 0 1
                                self.set_pin(pins[0],False)
                        else:
                                # Bad case
                                __clear()
                        sleep(self._T)
