"""
This is the source code of group 5 in the "Integrationsseminar" with the robotname Mr. Robot
Teammembers: Marco Schreiner, Max Sauer, Boas Luke Ruoss, Marco Zimmerer, Peter Walz, Christian Finkbeiner
"""

"""
Procedure: 1.init Robot 2.driving forward 3.if cross line -> activate camera 4.drive to animal + actiavate ultrasonic sensor
           5.if ultraonsic scan animal -> drive forward for fleeing animal + deativate ultrasonic + activate lineSensor 6. if across the line, timesleep 5sec + drive backwards
"""

import time 
import pigpio
import threading
from subprocess import call
from driving import Driver
from sensorControl import AnimalSelector
from sensorControl import LineSensor

class Robot:
        
    def __init__(self, selectedAnimal = "none"):
        self.selectedAnimal = selectedAnimal
        self.driver = Driver()
        self.lineSensor = LineSensor()
        self.animalSelector = AnimalSelector()
        self.pi = pigpio.pi()

    
    def start(self):

        self.animalSelector.getSelectedAnimal()

        if self.animalSelector.selectedAnimal == "none":
            call('sudo shutdown', shell=True)

        print(self.animalSelector.selectedAnimal)

        
        drivingThread = threading.Thread(target=self.driver.driveForward("fast")).start()
        self.lineSensor.runLineChecker()
        
        while self.lineSensor.lineCrossed == False:
            #wait for crossing the line
            print('--------------------------------------------------------------------')

        self.driver.stopDriving()

        print('--------------------------------------------------------------------')
        print('finished starting function')
        print('--------------------------------------------------------------------')


    def catchAnimal(self):                                  # has to be changed
        
        drivingThread = threading.Thread(target=self.driver.driveForward("medium"))

        #detectionThread = threading.Thread(target=XXX)


        drivingThread.start()
        #detectionThread.start()

        animalCatched = False

        while animalCatched == False:       #animal is in middle-bottom area of camera

            if animalScan == [self.animalSelector.selectedAnimal, "left", "top"] || animalScan == [self.animalSelector.selectedAnimal, "left", "middle"] || animalScan == [self.animalSelector.selectedAnimal, "left", "bottom"]:
                self.driver.turnLeft("slow")
                time.sleep(0.5)
                self.driver.driveForward("slow")
                pass

            elif animalScan == [self.animalSelector.selectedAnimal, "right", "top"] || animalScan == [self.animalSelector.selectedAnimal, "right", "middle"] || animalScan == [self.animalSelector.selectedAnimal, "right", "bottom"]:
                self.driver.turnRight("slow")
                time.sleep(0.5)
                self.driver.driveForward("slow")
                pass

            elif animalScan == [self.animalSelector.selectedAnimal, "middle", "top"]:
                self.driver.driveForward("fast")
                time.sleep(1)
                pass

            elif animalScan == [self.animalSelector.selectedAnimal, "middle", "middle"]:
                self.driver.driveForward("medium")
                time.sleep(1)
                pass

            elif animalScan == [self.animalSelector.selectedAnimal, "middle", "bottom"]:
                time.sleep(1)           #maybe should continue driving for 1 seconds that the animal is for sure in front of the robot
                animalCatched = True

            else:
                print("something went wrong. Pi will Shutdown now")
                self.pi.stop()

        self.driver.stopDriving()

        print('--------------------------------------------------------------------')
        print('finished catching function')
        print('--------------------------------------------------------------------')


    def freeAnimal(self):

        drivingThread = threading.Thread(target=self.driver.driveForward("fast"))

        drivingThread.start()
        self.lineSensor.runLineChecker()

        while self.lineSensor.lineCrossed == False:
            #wait for crossing the line
            print('--------------------------------------------------------------------')
        
        time.sleep(0.5)
        drivingThread = threading.Thread(target=self.driver.stopDriving()).start()
        print('--------------------------------------------------------------------')
        print('Robot is stopped')        
        print('--------------------------------------------------------------------')
        time.sleep(1)
        drivingThread = threading.Thread(target=self.driver.driveBackwards("fast")).start()
        print('--------------------------------------------------------------------')
        print('Robot will drive away from the animal')
        print('--------------------------------------------------------------------')
        time.sleep(2)
        drivingThread = threading.Thread(target=self.driver.stopDriving()).start()
        print('--------------------------------------------------------------------')
        print('Robot is stopped | finished catching animal, shutting down Pi...')
        print('--------------------------------------------------------------------')
        time.sleep(5)
        print("just joking ;)")


    # Let's go robot!

    def goRobot(self):
        self.start()
        self.catchAnimal()
        self.freeAnimal()


"""
Testing Area of the Script
"""

TestRobot = Robot()
#TestRobot.goRobot()
TestRobot.start()
TestRobot.freeAnimal()

