"""
This is the source code of group 5 in the "Integrationsseminar" with the robotname Mr. Robot
Teammembers: Marco Schreiner, Max Sauer, Boas Luke Ruoss, Marco Zimmerer, Peter Walz, Christian Finkbeiner
"""

class Robot:
        
    def __init__(self, Motor1_Rate = 0, Motor2_Rate = 0, speed_frontLeft = 0, speed_frontRight = 0, borderCrossed = False, selectedAnimal = "none"):
        self.Motor1_Rate = Motor1_Rate
        self.Motor2_Rate = Motor2_Rate
        self.speed_frontLeft = speed_frontLeft
        self.speed_frontRight = speed_frontRight
        self.borderCrossed = borderCrossed
        self.selectedAnimal = selectedAnimal

    #Setter and Getter for Speed

    def set_speed_frontLeft(self, speedLeft):               #Here has to be added an if condition that is used to calibrate the robot
        self.speed_frontLeft = speedLeft
        print("Speed-Left is now set to: ", speedLeft)

    def set_speed_frontRight(self, speedRight):             #Here has to be added an if condition that is used to calibrate the robot
        self.speed_frontRight = speedRight
        print("Speed-Right is now set to: ", speedRight)

    def get_speed_frontLeft(self):
        return self.speed_frontLeft

    def get_speed_frontRight(self):
        return self.speed_frontRight

    #driving functions
    """
    The robot will drive into the direction of the selected animal. In this case there are 5 different sections in the camera to get the right direction: straight lef, soft left, straight forward, soft right, straight right. After we got the animal and drive it out of the are we have to drive away from the animal
    """
    #Placeholder for speed forward: 1 slow, 2 normal, 3 fast; stop: 0; backwards: -1 slow, -2 medium, -3 fast

    def driveForward(self, rateForward):

        #current speed is different to the speed needed 
        if self.speedChecker(rateForward, True) == False:

            if rateForward == "slow":
                self.set_speed_frontLeft(1)
                self.set_speed_frontRight(1)

            elif rateForward == "medium":
                self.set_speed_frontLeft(2)
                self.set_speed_frontRight(2)

            elif rateForward == "hard":
                self.set_speed_frontLeft(3)
                self.set_speed_frontRight(3)

        #speed is already set
        else:
            pass

    def driveBack(self, rateBackwards):

        #current speed is different to the speed needed
        if self.speedChecker(rateBackwards, False) == False:

            if rateBackwards == "slow":
                self.set_speed_frontLeft(-1)
                self.set_speed_frontRight(-1)

            elif rateBackwards == "medium":
                self.set_speed_frontLeft(-2)
                self.set_speed_frontRight(-2)

            elif rateBackwards == "hard":
                self.set_speed_frontLeft(-3)
                self.set_speed_frontRight(-3)

        #speed is already set
        else:
            pass

    def turn(self, direction, rate):

        if self.directionChecker(direction, rate) == False:

            if direction == "left" and rate == "soft":
                self.set_speed_frontLeft(2)
                self.set_speed_frontRight(3)

            elif direction == "left" and rate == "hard":
                self.set_speed_frontLeft(1)
                self.set_speed_frontRight(3)

            elif direction == "right" and rate == "soft":
                self.set_speed_frontLeft(3)
                self.set_speed_frontRight(2)

            elif direction == "right" and rate == "hard":
                self.set_speed_frontLeft(3)
                self.set_speed_frontLeft(1)

        else: 
            pass

    def stopDriving(self):
        self.set_speed_frontLeft(0)
        self.set_speed_frontRight(0)

    #Functions to check the direction and the speed of the robot 

    def speedChecker(self, rate, ahead):
        
        #check for driving ahead or backwards
        if ahead == False:
            Holder_speed_frontLeft = self.get_speed_frontLeft() * -1
            Holder_speed_frontRight = self.get_speed_frontRight() * -1

        else:
            Holder_speed_frontLeft = self.get_speed_frontLeft()
            Holder_speed_frontRight = self.get_speed_frontRight()

        #check for speed
        if rate == "slow" and Holder_speed_frontLeft == 1 and Holder_speed_frontRight == 1:
            return True

        elif rate == "medium" and Holder_speed_frontLeft == 2 and Holder_speed_frontRight == 2:
            return True

        elif rate == "hard" and Holder_speed_frontLeft == 3 and Holder_speed_frontRight == 3: 
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

    #functions for sensors 

    def checkBorder(self):

        self.sensorData == True

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

    def animalCatched(self):
        return False

    #function inside the area for catching the animal

    def catchAnimal(self):
        self.getSelectedAnimal()
        self.Scan()
        self.checkDirection()

        while Sensorfront == False:
            self.checkDirection()
        else:
            self.stopDriving()
            self.closePress()
        
        while NoneAnimalinScreen == True:
            return true                 #insert function to check if there are other animals in screen and how to get them out of the screen.
        else:
            self.driveForward("Fast")
        
        while self.borderCrossed == False:
            self.checkBorder()
        else:
            pause()
            self.stopDriving()
    
    def freeAnimal(self):
        self.openPress()
        self.driveBack("fast")
        pause()
        self.stopDriving

    def dance(self):                    #a little easter egg function
        self.set_speed_frontLeft(3)
        self.set_speed_frontRight(-3)
        pause()
        self.stopDriving()
    
    def start(self):

        while self.borderCrossed == False:
            self.driveForward("fast")
            self.checkBorder()
        
        else:
            self.borderCrossed == False #Setting borderCrossed on false after you crossed it

    #Let's go robot!

    def goRobot(self):
        self.start()
        self.catchAnimal()
        self.freeAnimal()
        self.dance()


"""
Testing Area of the Script
"""


Mr_Robot = Robot()
# Mr_Robot.start()
Mr_Robot.driveForward("slow")