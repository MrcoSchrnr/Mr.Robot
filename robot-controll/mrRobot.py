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
from threading import Thread, Lock
from subprocess import call
from driving import Driver
from sensorControl import AnimalSelector
from sensorControl import LineSensor
from objectDetection import ObjectDetector


class Robot:
        
    def __init__(self):
        self.driver = Driver()
        self.lineSensor = LineSensor()
        self.animalSelector = AnimalSelector()
        self.objectDetector = ObjectDetector()
        self.pi = pigpio.pi()
        self.animalCatched = False

    
    def start(self):

        self.animalSelector.getSelectedAnimal()

        if self.animalSelector.selectedAnimal == "none":
            print("Something went wront. Shutting down RPi.")
            time.sleep(5)
            #call('sudo shutdown -h now', shell=True)

        print(self.animalSelector.selectedAnimal)

        lineSensorThread = Thread(target=self.lineSensor.runLineChecker)
        drivingThread = Thread(target=self.driver.driveForward, args=["fast"])

        lineSensorThread.start()
        drivingThread.start()

        lineSensorThread.join()
        drivingThread.join()
        
        while self.lineSensor.lineCrossed == False:
            #wait for crossing the line
            print('--------------------------------------------------------------------')
            continue

        drivingThread._stop()
        self.driver.stopDriving()

        print('--------------------------------------------------------------------')
        print('finished starting function')
        print('--------------------------------------------------------------------')

    
    def catchAnimal(self):                                  
        
        detectionThread = Thread(target=self.objectDetector.startDetector, args=["object-detection/yolov3/yolov3/64_v4/yolov3-tiny_last.weights", "object-detection/yolov3/yolov3/64_v4/team5.names", "object-detection/yolov3/yolov3/64_v4/team5.cfg", 256, 192])
        drivingThread = Thread(target=self.driver.driveForward, args=["slow"])
        lineSensorThread = Thread(target=self.lineSensor.runLineChecker, daemon=True)

        detectionThread.start()
        time.sleep(1)

        drivingThread.start()
        detectionThread.join()
        drivingThread.join()
        lineSensorThread.start()

        goOn = True

        while goOn == True: 

            if self.lineSensor.lineCrossed == True:
                time.sleep(0.5)
                drivingThread._stop()
                self.driver.stopDriving()
                time.sleep(0.5)

                self.driver.driveBackwards("fast")
                time.sleep(3)

                self.driver.stopDriving()

                #pi shutdown has to be inserted 

            else:
                self.objectDetector.get_label_map()
                counter = 0

                print(self.objectDetector.animalArray)
                for x in self.objectDetector.animalArray:
                    
                    print(self.animalSelector.selectedAnimal)
                    print(type(self.animalSelector.selectedAnimal))
                    print(x)
                    print(type(x))
                    print('--------------------------------------------------------------------')

                    if x == self.animalSelector.selectedAnimal:
                        verticalPosition = self.objectDetector.verticalPositionArray[counter]
                        horizontalPosition = self.objectDetector.horizontalPositionArray[counter]

                        print("vertikale Position des ", self.animalSelector.selectedAnimal, "s: ", verticalPosition)
                        print("horizontale Position des ", self.animalSelector.selectedAnimal, "s: ", horizontalPosition)
                        self.driver.stopDriving()

                        if horizontalPosition == "left":
                            self.driver.turnLeft()
                            time.sleep(0.25)
                        
                        elif horizontalPosition == "right":
                            self.driver.turnRight()
                            time.sleep(0.25)

                        elif horizontalPosition == "middle" and verticalPosition == "middle":
                            self.driver.driveForward("fast")
                            time.sleep(1.5)
                            self.animalCatched = True

                        elif horizontalPosition == "middle" and verticalPosition == "bottom":
                            self.animalCatched = True

                        else:
                            self.driver.driveForward("medium")
                            time.sleep(1.0)

                    counter += 1
                
                else:
                    self.driver.driveForward("medium")
                    time.sleep(1.0)
                    self.driver.stopDriving()


                self.objectDetector.resetArrays()

                goOn = not self.animalCatched
                continue

        self.driver.stopDriving()
        print('--------------------------------------------------------------------')
        print('finished catching function')
        print('--------------------------------------------------------------------')
    


    def freeAnimal(self):
        
        lineSensorThread = Thread(target=self.lineSensor.runLineChecker)
        drivingThread = Thread(target=self.driver.driveForward, args=["fast"])

        lineSensorThread.start()
        drivingThread.start()

        lineSensorThread.join()
        drivingThread.join()

        while self.lineSensor.lineCrossed == False:
            #wait for crossing the line
            print('--------------------------------------------------------------------')
        
        time.sleep(0.5)
        drivingThread._stop()
        self.driver.stopDriving()
        time.sleep(0.5)

        self.driver.driveBackwards("fast")
        time.sleep(3)

        self.driver.stopDriving()
        print('--------------------------------------------------------------------')
        print('Robot is stopped | finished catching animal, shutting down Pi...')
        print('--------------------------------------------------------------------')
        
        time.sleep(5)

        #shut down Pi for new Round
        #call('sudo shutdown -h now', shell=True)


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

