import time
from threading import Thread
from engineControl import Engines

class Driver:


    def __init__(self, speedBack = 0, speedLeft = 0, speedRight = 0):
        self.speedBack = speedBack
        self.speedLeft = speedLeft
        self.speedRight = speedRight
        self.engines = Engines()


    # duty cycle for slow = 5
    # duty cycle for medium = 10
    # duty cycle for fast = 90


    def driveForward(self, rate):

        if rate == "slow":
            engineLeftThread = Thread(target=self.engines.setSpeedLeft, args=[True, 50000, 5])
            engineRightThread = Thread(target=self.engines.setSpeedRight, args=[True, 50000, 5])
            engineBackThread = Thread(target=self.engines.stopEngineBack)  

            # start all threads
            engineLeftThread.start()
            engineRightThread.start()
            engineBackThread.start()

            # synchronize all threads
            engineLeftThread.join()
            engineRightThread.join()
            engineBackThread.join()

        elif rate == "medium":
            engineLeftThread = Thread(target=self.engines.setSpeedLeft, args=[True, 50000, 10])
            engineRightThread = Thread(target=self.engines.setSpeedRight, args=[True, 50000, 10])
            engineBackThread = Thread(target=self.engines.stopEngineBack) 
            
            # start all threads
            engineLeftThread.start()
            engineRightThread.start()
            engineBackThread.start()

            # synchronize all threads
            engineLeftThread.join()
            engineRightThread.join()
            engineBackThread.join()

        elif rate == "fast":
            engineLeftThread = Thread(target=self.engines.setSpeedLeft, args=[True, 50000, 90])
            engineRightThread = Thread(target=self.engines.setSpeedRight, args=[True, 50000, 90])
            engineBackThread = Thread(target=self.engines.stopEngineBack) 
            
            # start all threads
            engineLeftThread.start()
            engineRightThread.start()
            engineBackThread.start()

            # synchronize all threads
            engineLeftThread.join()
            engineRightThread.join()
            engineBackThread.join()

        else:
            print('Error. No rate selected.')          


    def driveBackwards(self, rate):

        if rate == "slow":
            engineLeftThread = Thread(target=self.engines.setSpeedLeft, args=[False, 50000, 5])
            engineRightThread = Thread(target=self.engines.setSpeedRight, args=[False, 50000, 5])
            engineBackThread = Thread(target=self.engines.stopEngineBack) 
            
            # start all threads
            engineLeftThread.start()
            engineRightThread.start()
            engineBackThread.start()

            # synchronize all threads
            engineLeftThread.join()
            engineRightThread.join()
            engineBackThread.join()

        elif rate == "medium":
            engineLeftThread = Thread(target=self.engines.setSpeedLeft, args=[False, 50000, 10])
            engineRightThread = Thread(target=self.engines.setSpeedRight, args=[False, 50000, 10])
            engineBackThread = Thread(target=self.engines.stopEngineBack) 
            
            # start all threads
            engineLeftThread.start()
            engineRightThread.start()
            engineBackThread.start()

            # synchronize all threads
            engineLeftThread.join()
            engineRightThread.join()
            engineBackThread.join()

        elif rate == "fast":
            engineLeftThread = Thread(target=self.engines.setSpeedLeft, args=[False, 50000, 90])
            engineRightThread = Thread(target=self.engines.setSpeedRight, args=[False, 50000, 90])
            engineBackThread = Thread(target=self.engines.stopEngineBack) 
            
            # start all threads
            engineLeftThread.start()
            engineRightThread.start()
            engineBackThread.start()

            # synchronize all threads
            engineLeftThread.join()
            engineRightThread.join()
            engineBackThread.join()

        else:
            print('Error. No rate selected.') 
    

    def driveLeft(self, rate):
        if rate == "slow":
            engineLeftThread = Thread(target=self.engines.setSpeedLeft, args=[True, 50000, 5])
            engineRightThread = Thread(target=self.engines.setSpeedRight, args=[True, 50000, 5])
            engineBackThread = Thread(target=self.engines.setSpeedBack, args=[True, 50000, 10])
            
            # start all threads
            engineLeftThread.start()
            engineRightThread.start()
            engineBackThread.start()

            # synchronize all threads
            engineLeftThread.join()
            engineRightThread.join()
            engineBackThread.join()

        elif rate == "medium":
            engineLeftThread = Thread(target=self.engines.setSpeedLeft, args=[True, 50000, 10])
            engineRightThread = Thread(target=self.engines.setSpeedRight, args=[True, 50000, 10])
            engineBackThread = Thread(target=self.engines.setSpeedBack, args=[True, 50000, 10]) 
            
            # start all threads
            engineLeftThread.start()
            engineRightThread.start()
            engineBackThread.start()

            # synchronize all threads
            engineLeftThread.join()
            engineRightThread.join()
            engineBackThread.join()

        elif rate == "fast":
            engineLeftThread = Thread(target=self.engines.setSpeedLeft, args=[True, 50000, 90])
            engineRightThread = Thread(target=self.engines.setSpeedRight, args=[True, 50000, 90])
            engineBackThread = Thread(target=self.engines.setSpeedBack, args=[True, 50000, 10]) 
            
            # start all threads
            engineLeftThread.start()
            engineRightThread.start()
            engineBackThread.start()

            # synchronize all threads
            engineLeftThread.join()
            engineRightThread.join()
            engineBackThread.join()

        else:
            print('Error. No rate selected.')      
    

    def driveRight(self, rate):
        if rate == "slow":
            engineLeftThread = Thread(target=self.engines.setSpeedLeft, args=[True, 50000, 5])
            engineRightThread = Thread(target=self.engines.setSpeedRight, args=[True, 50000, 5])
            engineBackThread = Thread(target=self.engines.setSpeedBack, args=[False, 50000, 10])
            
            # start all threads
            engineLeftThread.start()
            engineRightThread.start()
            engineBackThread.start()

            # synchronize all threads
            engineLeftThread.join()
            engineRightThread.join()
            engineBackThread.join()

        elif rate == "medium":
            engineLeftThread = Thread(target=self.engines.setSpeedLeft, args=[True, 50000, 10])
            engineRightThread = Thread(target=self.engines.setSpeedRight, args=[True, 50000, 10])
            engineBackThread = Thread(target=self.engines.setSpeedBack, args=[False, 50000, 10]) 
            
            # start all threads
            engineLeftThread.start()
            engineRightThread.start()
            engineBackThread.start()

            # synchronize all threads
            engineLeftThread.join()
            engineRightThread.join()
            engineBackThread.join()

        elif rate == "fast":
            engineLeftThread = Thread(target=self.engines.setSpeedLeft, args=[True, 50000, 90])
            engineRightThread = Thread(target=self.engines.setSpeedRight, args=[True, 50000, 90])
            engineBackThread = Thread(target=self.engines.setSpeedBack, args=[False, 50000, 10])
            
            # start all threads
            engineLeftThread.start()
            engineRightThread.start()
            engineBackThread.start()

            # synchronize all threads
            engineLeftThread.join()
            engineRightThread.join()
            engineBackThread.join()

        else:
            print('Error. No rate selected.')      


    def turnLeft(self, rate):
        engineLeftThread = Thread(target=self.engines.setSpeedLeft, args=[False, 50000, 5])
        engineRightThread = Thread(target=self.engines.setSpeedRight, args=[True, 50000, 5])
        engineBackThread = Thread(target=self.engines.setSpeedBack, args=[True, 50000, 10])
        
        # start all threads
        engineLeftThread.start()
        engineRightThread.start()
        engineBackThread.start()

        # synchronize all threads
        engineLeftThread.join()
        engineRightThread.join()
        engineBackThread.join()


    def turnRight(self, rate):
        engineLeftThread = Thread(target=self.engines.setSpeedLeft, args=[True, 50000, 5])
        engineRightThread = Thread(target=self.engines.setSpeedRight, args=[False, 50000, 5])
        engineBackThread = Thread(target=self.engines.setSpeedBack, args=[False, 50000, 10])
                
        # start all threads
        engineLeftThread.start()
        engineRightThread.start()
        engineBackThread.start()

        # synchronize all threads
        engineLeftThread.join()
        engineRightThread.join()
        engineBackThread.join()


    def stopDriving(self):
        self.engines.stopAllEngines()

TestDriver = Driver()
#TestDriver.driveForward("slow")
#time.sleep(1)
#TestDriver.stopDriving()
