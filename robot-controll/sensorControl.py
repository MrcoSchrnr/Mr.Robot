import pigpio
import time

#class AnimalSelector:


class LightSensor:

    def __init__(self, GPIO_LIGHT = 3, tally = 0, last_tick = 0, IGNORE_INTERVAL = 5000, HIGH = 1):
        self.GPIO_LIGHT = GPIO_LIGHT # Lightsensor GPIO pin
        self.IGNORE_INTERVAL = IGNORE_INTERVAL # microseconds
        self.HIGH = HIGH # returns HIGH for black and LOW for WHITE
        self.tally = tally # counter for callback function calls
        self.last_tick = last_tick # time of last valid callback function call
        self.pi = pigpio.pi()
    

    def level_changed(self, gpio_num, level, tick):
        self.tally += 1 

        if ((self.pi.read(gpio_num) == self.HIGH) and (tick - self.last_tick > self.IGNORE_INTERVAL)):
            print(f"{level} {self.tally} {((tick-self.last_tick)/1000000.):0.2f}")
            self.last_tick = tick


    def scan(self):
        self.pi.set_mode(self.GPIO_LIGHT, pigpio.INPUT)

        # Only LOW to HIGH is considered (rising edge). See logic in callback.
        # Callback must be adapted for considering falling edge.
        cb = self.pi.callback(self.GPIO_LIGHT, pigpio.RISING_EDGE, self.level_changed)

        while True:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                print('User interrupt')
                break;


    def stop(self):
        print('Shutting down LightSensor.')
        self.pi.stop()


    def checkBorder(self):
        while self.scan() != True:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                print('User interrupt')
                break;

        print('Robot crossed border.')
        self.stop()


#class UltraSensor:
    



TestSensor = LightSensor()
TestSensor.scan()
