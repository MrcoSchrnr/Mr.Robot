"""
This is the source code of group 5 in the "Integrationsseminar" with the robotname Mr. Robot
Teammembers: Marco Schreiner, Max Sauer, Boas Luke Ruoss, Marco Zimmerer, Peter Walz, Christian Finkbeiner
"""

#general functions and setup of the variables

motor1_rate = 0
speed_frontRight = 0
speed_frontLeft = 0

#driving functions
"""
The robot will drive into the direction of the selected animal. In this case there are 5 different sections in the camera to get the right direction: straight lef, soft left, straight forward, soft right, straight right. After we got the animal and drive it out of the are we have to drive away from the animal
"""

#Setter and Getter for Speed

def set_speed_frontLeft(speedLeft):
    speed_frontLeft = speedLeft

def set_speed_frontRight(speedRight):
    speed_frontRight = speedRight

def get_speed_frontLeft():
    return speed_frontLeft

def get_speed_frontRight():
    return speed_frontRight

#driving functions for Mr.Robot 
#Placeholder for speed forward: 1 slow, 2 normal, 3 fast; stop: 0; backwards: -1 slow, -2 medium, -3 fast

def speedChecker(rate, ahead):
    
    #check for driving ahead or backwards
    if ahead == False:
        Holder_speed_frontLeft = get_speed_frontLeft() * -1
        Holder_speed_frontRight = get_speed_frontRight() * -1

    else:
        Holder_speed_frontLeft = get_speed_frontLeft()
        Holder_speed_frontRight = get_speed_frontRight()

    #check for speed
    if rate == "slow" and Holder_speed_frontLeft == 1 and Holder_speed_frontRight == 1:
        return True

    elif rate == "medium" and Holder_speed_frontLeft == 2 and Holder_speed_frontRight == 2:
        return True

    elif rate == "hard" and Holder_speed_frontLeft == 3 and Holder_speed_frontRight == 3: 
        return True

    else:
        return False

#def directionChecker(direction):

def driveForward(rateForward):
    
    print(rateForward)
    print(speedChecker(rateForward, True))

    #current speed is different to the speed needed 
    if speedChecker(rateForward, True) == False:

        if rateForward == "slow":
            set_speed_frontLeft(1)
            set_speed_frontRight(1)

        elif rateForward == "medium":
            set_speed_frontLeft(2)
            set_speed_frontRight(2)

        elif rateForward == "hard":
            set_speed_frontLeft(3)
            set_speed_frontRight(3)

    #speed is already set
    else:
        pass

def driveBack(rateBackwards):

    print(rateBackwards)
    print(speedChecker(rateBackwards, False))

    #current speed is different to the speed needed
    if speedChecker(rateBackwards, False) == False:

        if rateBackwards == "slow":
            set_speed_frontLeft(-1)
            set_speed_frontRight(-1)

        elif rateBackwards == "medium":
            set_speed_frontLeft(-2)
            set_speed_frontRight(-2)

        elif rateBackwards == "hard":
            set_speed_frontLeft(-3)
            set_speed_frontRight(-3)

    #speed is already set
    else:
        pass

#def driveLeft(rate)

#def driveRight(rate)

"""
maybe we don't need this function, because we push the animal out of the area

def stopDriving():
    get_speed_frontLeft()
    get_speed_frontRight()

    if speed_frontLeft != 0 and speed_frontRight != 0:
        set_speed_frontLeft(0)
        set_speed_frontRight(0)
    else:
        pass

"""

#testing area

for counter in range(10):

    if counter == 0:
        driveForward("hard")

    elif counter == 2:
        driveBack("medium")

    elif counter == 4:
        driveForward("slow")

    else:
        pass

    print("SpeedLeft:")
    print(get_speed_frontLeft())
    print("SpeedRight:")
    print(get_speed_frontRight())
    print("-----------------------------------------------------------------")