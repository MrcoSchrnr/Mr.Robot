import pigpio
import time
import threading
import functools

#class AnimalSelector:


class LightSensor:

    def __init__(self, GPIO_LIGHT = 3, colorStop = 1):
        self.GPIO_LIGHT = GPIO_LIGHT # Lightsensor GPIO pin
        self.colorStop = colorStop # returns 1 for black and 0 for WHITE
        self.pi = pigpio.pi()
        self.lineCrossed = False
    

    def levelChanged(self, gpio_num, level, tick):

        lineValue = self.pi.read(gpio_num)
        if (lineValue == self.colorStop):
            self.lineCrossed = True


    def runLineChecker(self):
        
        self.pi.set_mode(self.GPIO_LIGHT, pigpio.INPUT)
        cb = self.pi.callback(self.GPIO_LIGHT, pigpio.RISING_EDGE, self.levelChanged)
        
        while self.lineCrossed == False:
            time.sleep(1)
            print("Waiting for crossing Line.")
            print('--------------------------------------------------------------------')

        print('Robot crossed line.')
        self.stop()

    def stop(self):
        print('Shutting down LightSensor.')
        print('--------------------------------------------------------------------')
        self.pi.stop()


#class UltraSensor:
