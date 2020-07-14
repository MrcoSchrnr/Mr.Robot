import pigpio
import time
from threading import Thread

class Engines:


    def __init__(self, Direction = "none", AheadBack = True, AheadLeft = True, AheadRight = True, FrequencyBack = 0, FrequencyLeft = 0, FrequencyRight = 0, DutyCycleBack = 0, DutyCycleLeft = 0, DutyCycleRight = 0, PWM_BACK = 18, PWM_LEFT = 13, PWM_RIGHT = 12, IN1_BACK = 6,IN1_LEFT = 27, IN1_RIGHT = 24, IN2_BACK = 5, IN2_LEFT = 22, IN2_RIGHT = 23):
        self.Direction = Direction
        self.AheadBack = AheadBack
        self.AheadLeft = AheadLeft
        self.AheadRight = AheadRight
        self.FrequencyBack = FrequencyBack
        self.FrequencyLeft = FrequencyLeft
        self.FrequencyRight = FrequencyRight
        self.DutyCycleBack = DutyCycleBack
        self.DutyCycleLeft = DutyCycleLeft
        self.DutyCycleRight = DutyCycleRight

        # set GPIO PINS

        self.PWM_BACK = PWM_BACK
        self.PWM_LEFT = PWM_LEFT
        self.PWM_RIGHT = PWM_RIGHT
        self.IN1_BACK = IN1_BACK
        self.IN1_LEFT = IN1_LEFT
        self.IN1_RIGHT = IN1_RIGHT
        self.IN2_BACK = IN2_BACK
        self.IN2_LEFT = IN2_LEFT
        self.IN2_RIGHT = IN2_RIGHT

        self.pi = pigpio.pi()

    """
        in this area there are the functions for the three engines (left, right and on the back).
        the functions will set the speed of the engines, the direction or stop them. 
    """

    # function for the engine on the back side 
    def setSpeedBack(self, ahead, frequency, dutyCycle):
        PWM_FREQUENCY = frequency #Hz
        PWM_DUTY_CYCLE = dutyCycle #percent

        if ahead == True:
            self.pi.set_mode(self.IN1_BACK, pigpio.OUTPUT)
            self.pi.set_mode(self.IN2_BACK, pigpio.OUTPUT)
            self.pi.write(self.IN1_BACK, 0)                       #has to be changed
            self.pi.write(self.IN2_BACK, 1)                       #has to be changed

        elif ahead == False:
            self.pi.set_mode(self.IN1_BACK, pigpio.OUTPUT)
            self.pi.set_mode(self.IN2_BACK, pigpio.OUTPUT)
            self.pi.write(self.IN1_BACK, 1)                       #has to be changed
            self.pi.write(self.IN2_BACK, 0)                       #has to be changed

        try:
            duty = PWM_DUTY_CYCLE * 10000 # Max: 1M
            self.pi.hardware_PWM (self.PWM_BACK, PWM_FREQUENCY, duty)
            print('Hardware PWM on GPIO ' + str(self.PWM_BACK) + ' enabled')
            print('Frequency: ' + str(self.pi.get_PWM_frequency(self.PWM_BACK)) + ' Hz')
            print('Dutycycle: ' + \
                    str(self.pi.get_PWM_dutycycle(self.PWM_BACK) / 10000) + ' percent')

        except: 
            print('Hardware PWM not available on GPIO ' + str(self.PWM_BACK))
            self.pi.stop()


    def stopEngineBack(self):
        self.pi.set_mode(self.IN1_BACK, pigpio.OUTPUT)
        self.pi.set_mode(self.IN2_BACK, pigpio.OUTPUT)

        self.pi.write(self.IN1_BACK, 1)
        self.pi.write(self.IN2_BACK, 1)

        print('The Engine on the back is now stopped.')


    def setSpeedLeft(self, ahead, frequency, dutyCycle):
            PWM_FREQUENCY = frequency #Hz
            PWM_DUTY_CYCLE = dutyCycle #percent

            if ahead == True:
                self.pi.set_mode(self.IN1_LEFT, pigpio.OUTPUT)
                self.pi.set_mode(self.IN2_LEFT, pigpio.OUTPUT)
                self.pi.write(self.IN1_LEFT, 0)                       #has to be changed
                self.pi.write(self.IN2_LEFT, 1)                       #has to be changed

            elif ahead == False:
                self.pi.set_mode(self.IN1_LEFT, pigpio.OUTPUT)
                self.pi.set_mode(self.IN2_LEFT, pigpio.OUTPUT)
                self.pi.write(self.IN1_LEFT, 1)                       #has to be changed
                self.pi.write(self.IN2_LEFT, 0)                       #has to be changed

            try:
                duty = PWM_DUTY_CYCLE * 10000 # Max: 1M
                self.pi.hardware_PWM (self.PWM_LEFT, PWM_FREQUENCY, duty)
                print('Hardware PWM on GPIO ' + str(self.PWM_LEFT) + ' enabled')
                print('Frequency: ' + str(self.pi.get_PWM_frequency(self.PWM_LEFT)) + ' Hz')
                print('Dutycycle: ' + \
                        str(self.pi.get_PWM_dutycycle(self.PWM_LEFT) / 10000) + ' percent')

            except: 
                print('Hardware PWM not available on GPIO ' + str(self.PWM_LEFT))
                self.pi.stop()


    def stopEngineLeft(self):
        self.pi.set_mode(self.IN1_LEFT, pigpio.OUTPUT)
        self.pi.set_mode(self.IN2_LEFT, pigpio.OUTPUT)

        self.pi.write(self.IN1_LEFT, 1)
        self.pi.write(self.IN2_LEFT, 1)

        print('The Engine on the left side is now stopped.')


    def setSpeedRight(self, ahead, frequency, dutyCycle):
            PWM_FREQUENCY = frequency #Hz
            PWM_DUTY_CYCLE = dutyCycle #percent

            if ahead == True:
                self.pi.set_mode(self.IN1_RIGHT, pigpio.OUTPUT)
                self.pi.set_mode(self.IN2_RIGHT, pigpio.OUTPUT)
                self.pi.write(self.IN1_RIGHT, 0)                       #has to be changed
                self.pi.write(self.IN2_RIGHT, 1)                       #has to be changed

            elif ahead == False:
                self.pi.set_mode(self.IN1_RIGHT, pigpio.OUTPUT)
                self.pi.set_mode(self.IN2_RIGHT, pigpio.OUTPUT)
                self.pi.write(self.IN1_RIGHT, 1)                       #has to be changed
                self.pi.write(self.IN2_RIGHT, 0)                       #has to be changed

            try:
                duty = PWM_DUTY_CYCLE * 10000 # Max: 1M
                self.pi.hardware_PWM (self.PWM_RIGHT, PWM_FREQUENCY, duty)
                print('Hardware PWM on GPIO ' + str(self.PWM_RIGHT) + ' enabled')
                print('Frequency: ' + str(self.pi.get_PWM_frequency(self.PWM_RIGHT)) + ' Hz')
                print('Dutycycle: ' + \
                        str(self.pi.get_PWM_dutycycle(self.PWM_RIGHT) / 10000) + ' percent')

            except: 
                print('Hardware PWM not available on GPIO ' + str(self.PWM_RIGHT))
                self.pi.stop()


    def stopEngineRight(self):
        self.pi.set_mode(self.IN1_RIGHT, pigpio.OUTPUT)
        self.pi.set_mode(self.IN2_RIGHT, pigpio.OUTPUT)

        self.pi.write(self.IN1_RIGHT, 1)
        self.pi.write(self.IN2_RIGHT, 1)

        print('The Engine on the right side is now stopped.')


    def stopAllEngines(self):
        engineBack = Thread(target=self.stopEngineBack)
        engineLeft = Thread(target=self.stopEngineLeft)
        engineRight = Thread(target=self.stopEngineRight)

        engineBack.start()
        engineLeft.start()
        engineRight.start()

        engineBack.join()
        engineLeft.join()
        engineRight.join()


    """ 
        in this area there are some additional funtions for shutting down the engines and getting the current data of the engines
    """

    def shutDown(self):
        #disable PWM
        self.pi.write(self.PWM_BACK, 0)
        self.pi.write(self.PWM_LEFT, 0)
        self.pi.write(self.PWM_RIGHT, 0)

        # Free resources
        self.pi.stop()


    def getData(self):
        dataArray = ["Direction: ", self.Direction, "Back (ahead, frequency, dutyCycle): ", self.AheadBack, self.FrequencyBack, self.DutyCycleBack, "Left (ahead, frequency, dutyCycle) :", self.AheadLeft, self.FrequencyLeft, self.DutyCycleLeft, "Right (ahead, frequency, dutyCycle) :", self.AheadRight, self.FrequencyRight, self.DutyCycleRight]
        return dataArray