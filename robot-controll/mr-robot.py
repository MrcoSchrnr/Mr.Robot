"""
This is the source code of group 5 in the "Integrationsseminar" with the robotname Mr. Robot
Teammembers: Marco Schreiner, Max Sauer, Boas Luke Ruoss, Marco Zimmerer, Peter Walz, Christian Finkbeiner
"""

import time 
import motorPWM2.py
import lightsensor_interrupt.py

class Robot:
        
    def __init__(self, speed_frontLeft = 0, speed_frontRight = 0, borderCrossed = False, selectedAnimal = "none", drivingDirection = "ahead"):
        self.speed_frontLeft = speed_frontLeft
        self.speed_frontRight = speed_frontRight
        self.borderCrossed = borderCrossed
        self.selectedAnimal = selectedAnimal
        self.drivingDirection = drivingDirection

    # Setter and Getter for Speed

    def set_speed_frontLeft(self, ahead, speedLeft):               # Here has to be added an if condition that is used to calibrate the robot
        ahead = ahead

        if speedLeft == 1:
            frequenzy == 50000

        elif speedLeft == 2:
            frequenzy == 60000
        
        elif speedLeft == 3:
            frequenzy == 70000
        
        # driving
        motorPWM2.drive(ahead, frequenzy, 10)
        
        # stop driving
        motorPWM2.stop()

    def set_speed_frontRight(self, speedRight):             # Here has to be added an if condition that is used to calibrate the robot
        self.speed_frontRight = speedRight

    def get_speed_frontLeft(self):
        return self.speed_frontLeft

    def get_speed_frontRight(self):
        return self.speed_frontRight

    # driving functions
    """
    The robot will drive into the direction of the selected animal. In this case there are 5 different sections in the camera to get the right direction: straight lef, soft left, straight forward, soft right, straight right. After we got the animal and drive it out of the are we have to drive away from the animal
    """
    # Placeholder for speed forward: 1 slow, 2 normal, 3 fast; stop: 0; backwards: -1 slow, -2 medium, -3 fast

    def driveForward(self, rateForward):

        #current speed is different to the speed needed 
        if self.speedChecker(rateForward, True) == False:

            if rateForward == "slow":
                self.set_speed_frontLeft(True, 1)
                self.set_speed_frontRight(True, 1)

            elif rateForward == "medium":
                self.set_speed_frontLeft(True, 2)
                self.set_speed_frontRight(True, 2)

            elif rateForward == "hard":
                self.set_speed_frontLeft(True, 3)
                self.set_speed_frontRight(True, 3)

        # speed is already set
        else:
            pass

    def driveBack(self, rateBackwards):

        # current speed is different to the speed needed
        if self.speedChecker(rateBackwards, False) == False:

            if rateBackwards == "slow":
                self.set_speed_frontLeft(False, 1)
                self.set_speed_frontRight(False,1)

            elif rateBackwards == "medium":
                self.set_speed_frontLeft(False, 2)
                self.set_speed_frontRight(False, 2)

            elif rateBackwards == "hard":
                self.set_speed_frontLeft(False, 3)
                self.set_speed_frontRight(False, 3)

        # speed is already set
        else:
            pass

    def turn(self, direction, rate):

        if self.directionChecker(direction, rate) == False:

            if direction == "left" and rate == "soft":
                self.set_speed_frontLeft(True, 2)
                self.set_speed_frontRight(True, 3)

            elif direction == "left" and rate == "hard":
                self.set_speed_frontLeft(True, 1)
                self.set_speed_frontRight(True, 3)

            elif direction == "right" and rate == "soft":
                self.set_speed_frontLeft(True, 3)
                self.set_speed_frontRight(True, 2)

            elif direction == "right" and rate == "hard":
                self.set_speed_frontLeft(True, 3)
                self.set_speed_frontLeft(True, 1)

        else: 
            pass

    def stopDriving(self):
        self.set_speed_frontLeft(True, 0)
        self.set_speed_frontRight(True, 0)

    # Functions to check the direction and the speed of the robot 

    def speedChecker(self, rate, ahead):

        # check for speed
        if ahead == False and rate == "slow" and get_speed_frontLeft() == -3 and get_speed_frontRight() == -3:
            return True

        elif ahead == False and rate == "hard" and get_speed_frontLeft() == -2 and get_speed_frontRight() == -2:
            return True

        elif ahead == False and rate == "slow" and get_speed_frontLeft() == -1 and get_speed_frontRight() == -1:
            return True

        elif ahead == True and rate == "slow" and get_speed_frontLeft() == -1 and get_speed_frontRight() == -1:
            return True

        elif ahead == True and rate == "medium" and get_speed_frontLeft() == -2 and get_speed_frontRight() == -2:
            return True

        elif ahead == True and rate == "hard" and get_speed_frontLeft() == -3 and get_speed_frontRight() == -3: 
            return True

        else:
            return False

    def directionChecker(self, direction, rate):

        if direction == "left" and rate == "hard" and self.get_speed_frontLeft == 1 and self.get_speed_frontRight == 3:
            return True

        elif direction == "left" and rate == "soft" and self.get_speed_frontLeft == 2 and self.get_speed_frontRight == 3:
            return True

        elif direction == "right" and rate == "soft" and self.get_speed_frontLeft == 3 and self.get_speed_frontRight == 2:
            return True

        elif direction == "right" and rate == "hard" and self.get_speed_frontLeft == 3 and self.get_speed_frontRight == 1:
            return True

        else:
            return False

    # functions for sensors 

    def checkBorder(self):

        if self.sensorData == True:
            self.borderCrossed == True
            return self.borderCrossed

        else: 
            pass

    def getSelectedAnimal(self):
        
        if selection == 1:
            self.selectedAnimal == "Tiger"
            return self.selectedAnimal

        elif selection == 2:
            self.selectedAnimal == "Elephant"
            return self.selectedAnimal

        elif selection == 3:
            self.selectedAnimal == "Frog"
            return self.selectedAnimal

        elif selection == 4:
            self.selectedAnimal == "Cat"
            return self.selectedAnimal

        elif selection == 5:
            self.selectedAnimal == "Star"
            return self.selectedAnimal

    # function inside the area for catching the animal

    def catchAnimal(self):
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

    def dance(self):                                # a little easter egg function
        self.set_speed_frontLeft(True, 3)
        self.set_speed_frontRight(False, 3)
        time.sleep(10)
        self.stopDriving()
    
    def start(self):

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
        self.dance()


"""
Testing Area of the Script
"""


Mr_Robot = Robot()
# Mr_Robot.goRobot()
Mr_Robot.driveForward("slow")