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

from driving import Driver
import lightsensor_interrupt


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

# Motor

                                                           #TODO: Pinout Motor

# Ultrasonic - @pre pigpio demon must be running (sudo pigpiod)

GPIO_Ultra_ECHO = 17 # ultrasonic sensor input pin (echo)
GPIO_Ultra_TRIG = 26 # ultrasonic sensor output pin (trigger)

# Lightsensor - @pre pigpio demon must be running (sudo pigpiod)

GPIO_LIGHT = 4 # Lightsensor GPIO pin

"""
End of Area Pinouts
"""

class Robot:
        
    def __init__(self, selectedAnimal = "none"):
        self.selectedAnimal = selectedAnimal
        self.driver = Driver()


    # functions for sensors 

    def checkBorder(self):                                  # has to be changed
        # define function for: none return from sensor -> false, else true

        if self.sensorData == True:
            self.borderCrossed == True
            return self.borderCrossed

        else: 
            pass

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
        self.getSelectedAnimal()
        self.Scan()
        self.checkDirection()

        while Sensorfront == False:
            self.checkDirection()

        else:
            self.driveForward("slow")
        
        while NoneAnimalinScreen == False:
            return true                             # insert function to check if there are other animals in screen and how to get them out of the screen.

        else:
            self.driveForward("Fast")
        
        while self.borderCrossed == False:
            self.checkBorder()

        else:
            time.sleep(5)
            self.stopDriving()
    
    def freeAnimal(self):
        self.driveBack("fast")
        time.sleep(5)
        self.stopDriving
    
    def start(self):

        #active line-sensor
        #deactivate camera
        #deactivate ultrasonic-sensor

        while self.borderCrossed == False:
            self.driveForward("fast")
            self.checkBorder()
        
        else:
            self.borderCrossed == False # Setting borderCrossed on false after you crossed it

    # Let's go robot!

    def goRobot(self):
        self.start()
        self.catchAnimal()
        self.freeAnimal()

    def reset(self):                                            # has to be changed
        return True                     # Function to reset the selected Animal; speed on Wheels and so on. 


"""
Testing Area of the Script
"""

Mr_Robot = Robot()
Mr_Robot.test()