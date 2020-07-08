import time
from threading import Thread
from engineControl import Engines

class Driver:


    def __init__(self, speedBack = 0, speedLeft = 0, speedRight = 0):
        self.speedBack = speedBack
        self.speedLeft = speedLeft
        self.speedRight = speedRight
        self.engines = Engines()


    # minimum duty cycle on wood ground is 5 that the robot moves. 


    def driveForward(self, rate):

        if rate == "slow":
            Thread(target=self.engines.setSpeedLeft(True, 50000, 5)).start()
            Thread(target=self.engines.setSpeedRight(True, 50000, 5)).start()
            Thread(target=self.engines.stopEngineBack()).start()  

        elif rate == "medium":
            Thread(target=self.engines.setSpeedLeft(True, 50000, 10)).start()
            Thread(target=self.engines.setSpeedRight(True, 50000, 10)).start()
            Thread(target=self.engines.stopEngineBack()).start()  

        elif rate == "fast":
            Thread(target=self.engines.setSpeedLeft(True, 50000, 80)).start()
            Thread(target=self.engines.setSpeedRight(True, 50000, 80)).start()
            Thread(target=self.engines.stopEngineBack()).start()  

        else:
            print('Error. No rate selected.')          


    def driveBackwards(self, rate):

        if rate == "slow":
            Thread(target=self.engines.setSpeedLeft(False, 50000, 5)).start()
            Thread(target=self.engines.setSpeedRight(False, 50000, 5)).start()
            Thread(target=self.engines.stopEngineBack()).start()  

        elif rate == "medium":
            Thread(target=self.engines.setSpeedLeft(False, 50000, 10)).start()
            Thread(target=self.engines.setSpeedRight(False, 50000, 10)).start()
            Thread(target=self.engines.stopEngineBack()).start()  

        elif rate == "fast":
            Thread(target=self.engines.setSpeedLeft(False, 50000, 80)).start()
            Thread(target=self.engines.setSpeedRight(False, 50000, 80)).start()
            Thread(target=self.engines.stopEngineBack()).start()  

        else:
            print('Error. No rate selected.') 
    

    def driveLeft(self, rate):
        if rate == "slow":
            Thread(target=self.engines.setSpeedLeft(True, 50000, 5)).start()
            Thread(target=self.engines.setSpeedRight(True, 50000, 5)).start()
            Thread(target=self.engines.setSpeedBack(True, 50000, 10)).start()

        elif rate == "medium":
            Thread(target=self.engines.setSpeedLeft(True, 50000, 10)).start()
            Thread(target=self.engines.setSpeedRight(True, 50000, 10)).start()
            Thread(target=self.engines.setSpeedBack(True, 50000, 10)).start()  

        elif rate == "fast":
            Thread(target=self.engines.setSpeedLeft(True, 50000, 80)).start()
            Thread(target=self.engines.setSpeedRight(True, 50000, 80)).start()
            Thread(target=self.engines.setSpeedBack(True, 50000, 10)).start()  

        else:
            print('Error. No rate selected.')      
    

    def driveRight(self, rate):
        if rate == "slow":
            Thread(target=self.engines.setSpeedLeft(True, 50000, 5)).start()
            Thread(target=self.engines.setSpeedRight(True, 50000, 5)).start()
            Thread(target=self.engines.setSpeedBack(False, 50000, 10)).start()

        elif rate == "medium":
            Thread(target=self.engines.setSpeedLeft(True, 50000, 10)).start()
            Thread(target=self.engines.setSpeedRight(True, 50000, 10)).start()
            Thread(target=self.engines.setSpeedBack(False, 50000, 10)).start()  

        elif rate == "fast":
            Thread(target=self.engines.setSpeedLeft(True, 50000, 80)).start()
            Thread(target=self.engines.setSpeedRight(True, 50000, 80)).start()
            Thread(target=self.engines.setSpeedBack(False, 50000, 10)).start()

        else:
            print('Error. No rate selected.')      


    def turnLeft(self, rate):
        Thread(target=self.engines.setSpeedLeft(False, 50000, 5)).start()
        Thread(target=self.engines.setSpeedRight(True, 50000, 5)).start()
        Thread(target=self.engines.setSpeedBack(True, 50000, 10)).start()


    def turnRight(self, rate):
        Thread(target=self.engines.setSpeedLeft(True, 50000, 5)).start()
        Thread(target=self.engines.setSpeedRight(False, 50000, 5)).start()
        Thread(target=self.engines.setSpeedBack(False, 50000, 10)).start()  


    def stopDriving(self):
        self.engines.stopAllEngines()