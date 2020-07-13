"""
This is the source code of group 5 in the "Integrationsseminar" with the robotname Mr. Robot
Teammembers: Marco Schreiner, Max Sauer, Boas Luke Ruoss, Marco Zimmerer, Peter Walz, Christian Finkbeiner
"""

"""
Procedure: 1.init Robot 2.driving forward 3.if cross line -> activate camera 4.drive to animal + actiavate ultrasonic sensor
           5.if ultraonsic scan animal -> drive forward for fleeing animal + deativate ultrasonic + activate lightsensor 6. if across the line, timesleep 5sec + drive backwards
"""

import time 
import pigpio
from threading import Thread
import threading

from driving import Driver
#from sensorControl import AnimalSelector
from sensorControl import LightSensor
#from sensorControl import UltraSensor


"""
Area Pinouts
"""

# Maybe ON/OFF

# Switch

GPIO_IN_Elephant = 0 # Switchposition 1 - Elephant          TODO: Check right Pin for X
 
GPIO_IN_Tiger = 0    # Switchposition 2 - Tiger

GPIO_IN_Star = 0     # Switchposition 3 - Star              TODO: Check right Pin for X
 
GPIO_IN_Cat = 5      # Switchposition 4 - Cat               TODO: Check right Pin for X

GPIO_IN_Frog = 0     # Switchposition 5 - Frog              TODO: Check right Pin for X


# Ultrasonic - @pre pigpio demon must be running (sudo pigpiod)

GPIO_Ultra_ECHO = 17 # ultrasonic sensor input pin (echo)
GPIO_Ultra_TRIG = 26 # ultrasonic sensor output pin (trigger)


"""
End of Area Pinouts
"""

class Robot:
        
    def __init__(self, selectedAnimal = "none"):
        self.selectedAnimal = selectedAnimal
        self.driver = Driver()
        self.lightSensor = LightSensor()
        #self.ultraSensor = UltraSensor()
        #self.animalSelector = AnimalSelector()


    # functions for sensors 

    def getSelectedAnimal(self):                            #TAKE CARE! Signal 0 = On. Signal 1 = OFF.
        
        self.pi = pigpio.pi()  

        selectedAnimal = "none"
      
        if self.pi.read(GPIO_IN_Elephant) == 0:
            selectedAnimal = "Elephant"        

        if self.pi.read(GPIO_IN_Tiger) == 0:
            selectedAnimal = "Tiger"

        if self.pi.read(GPIO_IN_Frog) == 0:
            selectedAnimal = "Frog"

        if self.pi.read(GPIO_IN_Cat) == 0:
            selectedAnimal = "Cat"

        if self.pi.read(GPIO_IN_Star) == 0:
            selectedAnimal = "Star"

        print("You choose the " + selectedAnimal)
        return selectedAnimal 

    # function inside the area for catching the animal

    def catchAnimal(self):                                  # has to be changed
        
        print('code for catching the animal has to be implemented')
        time.sleep(5)
    
    def freeAnimal(self):
        startDrivingThread = Thread(target=self.driver.driveForward("medium")).start()
        lightSensorThread = Thread(target=self.lightSensor.runLineChecker()).start()
        time.sleep(2)

        startDrivingFasterThread = Thread(target=self.driver.driveForward("fast")).start()

        while lightSensorThread == True:
            #wait for end of the light sensor thread
            print('wait for ending of lightSensorScript')
        
        time.sleep(2)
        stopDrivingThread = Thread(target=self.driver.stopDriving()).start()

        driveAwayThread = Thread(target=self.driver.driveBackwards("fast"))
        time.sleep(2)
        stopDrivingThread = Thread(target=self.driver.stopDriving()).start()

    
    def start(self):
        #getAnimalThread = Thread(target=self.animalSelector.isAnimalSelected())
        startDrivingThread = Thread(target=self.driver.driveForward("medium")).start()
        lightSensorThread = Thread(target=self.lightSensor.runLineChecker()).start()

        while lightSensorThread == True:
            #wait for end of the light sensor thread
            time.sleep(1)
            print('--------------------------------------------------------------------')

        stopDrivingThread = Thread(target=self.driver.stopDriving()).start()

    # Let's go robot!

    def goRobot(self):
        self.start()
        self.catchAnimal()
        self.freeAnimal()


"""
Testing Area of the Script
"""

TestRobot = Robot()
TestRobot.goRobot()

