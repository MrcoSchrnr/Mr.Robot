"""
This is the source code of group 5 in the "Integrationsseminar" with the robotname Mr. Robot
Teammembers: Marco Schreiner, Max Sauer, Boas Luke Ruoss, Marco Zimmerer, Peter Walz, Christian Finkbeiner
"""

import time 
import motor-LeftWheel
import motor-RightWheel
import motor-Back
import lightsensor_interrupt

class Robot:
        
    def __init__(self, speed_frontLeft = 0, speed_frontRight = 0, speed_Back = 0, borderCrossed = False, selectedAnimal = "none", drivingDirection = "ahead"):
        self.speed_frontLeft = speed_frontLeft
        self.speed_frontRight = speed_frontRight
        self.speed_Back = speed_Back
        self.borderCrossed = borderCrossed
        self.selectedAnimal = selectedAnimal
        self.drivingDirection = drivingDirection

    # Setter and Getter for Speed

    def set_speed_motorLeft(self, ahead, speedLeft):               # Here has to be added an if condition that is used to calibrate the robot        
        #adding different speed types
        
        # driving
        motor-LeftWheel.drive(ahead = ahead)
        
        # stop driving
        motor-LeftWheel.stop()

        #define String of self.speed_frontLeft
        self.speed_frontLeft = str(ahead, (" ", frequency, " ", duty))

    def set_speed_motorRight(self, ahead, speedRight):             # Here has to be added an if condition that is used to calibrate the robot
        #adding different speed types
        
        # driving
        motor-LeftWheel.drive(ahead = ahead)
        
        # stop driving
        motor-LeftWheel.stop()

        #define String of self.speed_frontRight
        self.speed_frontRight = str(ahead, (" ", frequency, " ", duty))

    # True = left; False = right
    def set_speed_motorBack(self, direction, speedLeft):           # Here has to be added an if condition that is used to calibrate the robot
        #adding different speed types
        
        # driving
        motor-Back.drive(direction = direction)
        
        # stop driving
        motor-Back.stop()

        #define String of self.speed_frontRight
        self.speed_Back = str(direction, (" ", frequency, " ", duty))

    def get_speed_motorLeft(self):
        self.speed_frontLeft = motor-LeftWheel.getData()
        return self.speed_frontLeft

    def get_speed_motorRight(self):
        self.speed_frontRight = motor-RightWheel.getData()
        return self.speed_frontRight

    def get_speed_motorBack(self):
        self.speed_Back = motor-Back.getData()
        return self.speed_Back

    # driving functions
    """
    The robot will drive into the direction of the selected animal. In this case there are 5 different sections in the camera to get the right direction: straight lef, soft left, straight forward, soft right, straight right. After we got the animal and drive it out of the are we have to drive away from the animal
    """
    # These functions has to be changed because of the 3rd wheel on the back

    # Placeholder for speed forward: 1 slow, 2 normal, 3 fast; stop: 0; backwards: -1 slow, -2 medium, -3 fast

    def driveForward(self, rateForward):

        #current speed is different to the speed needed 
        if self.speedChecker(rateForward, True) == False:

            if rateForward == "slow":
                self.set_speed_motorLeft(True, 1)
                self.set_speed_motorRight(True, 1)
                self.set_speed_motorBack(True, 0)

            elif rateForward == "medium":
                self.set_speed_motorLeft(True, 2)
                self.set_speed_motorRight(True, 2)
                self.set_speed_motorBack(True, 0)

            elif rateForward == "hard":
                self.set_speed_motorLeft(True, 3)
                self.set_speed_motorRight(True, 3)
                self.set_speed_motorBack(True, 0)

        # speed is already set
        else:
            pass

    def driveBack(self, rateBackwards):

        # current speed is different to the speed needed
        if self.speedChecker(rateBackwards, False) == False:

            if rateBackwards == "slow":
                self.set_speed_motorLeft(False, 1)
                self.set_speed_motorRight(False,1)
                self.set_speed_motorBack(True, 0)

            elif rateBackwards == "medium":
                self.set_speed_motorLeft(False, 2)
                self.set_speed_motorRight(False, 2)
                self.set_speed_motorBack(True, 0)

            elif rateBackwards == "hard":
                self.set_speed_motorLeft(False, 3)
                self.set_speed_motorRight(False, 3)
                self.set_speed_motorBack(True, 0)

        # speed is already set
        else:
            pass
    
    # maybe there has to be added an function für driving with same body position (body don't turn)
    def turn(self, direction, rate):                                # has to be changed

        if self.directionChecker(direction, rate) == False:

            if direction == "left" and rate == "soft":
                self.set_speed_motorLeft(True, 2)
                self.set_speed_motorRight(True, 3)

            elif direction == "left" and rate == "hard":
                self.set_speed_motorLeft(True, 1)
                self.set_speed_motorRight(True, 3)

            elif direction == "right" and rate == "soft":
                self.set_speed_motorLeft(True, 3)
                self.set_speed_motorRight(True, 2)

            elif direction == "right" and rate == "hard":
                self.set_speed_motorLeft(True, 3)
                self.set_speed_motorLeft(True, 1)

        else: 
            pass

    def stopDriving(self):
        self.set_speed_motorLeft(True, 0)
        self.set_speed_motorRight(True, 0)
        self.set_speed_motorBack(True, 0)

    # Functions to check the direction and the speed of the robot 
    # these function has to be changed as well because of the 3rd motor
    def speedChecker(self, rate, ahead):

        # check for speed
        if ahead == False and rate == "slow" and get_speed_motorLeft() == -3 and get_speed_motorRight() == -3:
            return True

        elif ahead == False and rate == "hard" and get_speed_motorLeft() == -2 and get_speed_motorRight() == -2:
            return True

        elif ahead == False and rate == "slow" and get_speed_motorLeft() == -1 and get_speed_motorRight() == -1:
            return True

        elif ahead == True and rate == "slow" and get_speed_motorLeft() == -1 and get_speed_motorRight() == -1:
            return True

        elif ahead == True and rate == "medium" and get_speed_motorLeft() == -2 and get_speed_motorRight() == -2:
            return True

        elif ahead == True and rate == "hard" and get_speed_motorLeft() == -3 and get_speed_motorRight() == -3: 
            return True

        else:
            return False

    def directionChecker(self, direction, rate):

        if direction == "left" and rate == "hard" and self.get_speed_motorLeft == 1 and self.get_speed_motorRight == 3:
            return True

        elif direction == "left" and rate == "soft" and self.get_speed_motorLeft == 2 and self.get_speed_motorRight == 3:
            return True

        elif direction == "right" and rate == "soft" and self.get_speed_motorLeft == 3 and self.get_speed_motorRight == 2:
            return True

        elif direction == "right" and rate == "hard" and self.get_speed_motorLeft == 3 and self.get_speed_motorRight == 1:
            return True

        else:
            return False

    # functions for sensors 

    def checkBorder(self):                                  # has to be changed
        # define function for: none return from sensor -> false, else true

        if self.sensorData == True:
            self.borderCrossed == True
            return self.borderCrossed

        else: 
            pass

    def getSelectedAnimal(self):                            # has to be changed
        selection = selectionScript.getData()               # has to be changed 

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

    def dance(self):                                # a little easter egg function but has to be changed for the motor on the back
        self.set_speed_motorLeft(True, 3)
        self.set_speed_motorRight(False, 3)
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

    def reset():                                            # has to be changed
        return True                     # Function to reset the selected Animal; speed on Wheels and so on. 

    def shutDown():
        motor-LeftWheel.shutDown()
        motor-RightWheel.shutDown()
        motor-Back.shutDown()

"""
Testing Area of the Script
"""


Mr_Robot = Robot()
# Mr_Robot.goRobot()
Mr_Robot.shutDown()