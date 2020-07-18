import pigpio
import time

class AnimalSelector:

    def __init__(self, elephantPin=14 , tigerPin=15, frogPin=16, catPin=20, starPin=21):

        """
            on the shifter we got the Pins 2, 14, 15, 16, 20 and 21 for selection. 
        """
        self.animalArray = [elephantPin, tigerPin, frogPin, catPin, starPin]
        self.elephantPin = elephantPin
        self.tigerPin = tigerPin
        self.frogPin = frogPin
        self.catPin = catPin
        self.starPin = starPin
        self.selectedAnimal = "none"
        self.pi = pigpio.pi()


    def checkPin(self, GPIO_PIN):
        self.pi.set_mode(GPIO_PIN, pigpio.OUTPUT)
        state = self.pi.read(GPIO_PIN)
        state = str(state)

        if state == str(1):
            self.selectedAnimal = GPIO_PIN
            return True
        else:
            return False
    
    def getSelectedAnimal(self):
        
        for x in self.animalArray:
            
            if self.checkPin(x) == True:
                
                if x == self.elephantPin:
                    self.selectedAnimal = "elephant"
                    return self.selectedAnimal
                
                elif x == self.tigerPin:
                    self.selectedAnimal = "tiger"
                    return self.selectedAnimal
                
                elif x == self.frogPin:
                    self.selectedAnimal = "frog"
                    return self.selectedAnimal

                elif x == self.catPin:
                    self.selectedAnimal = "cat"
                    return self.selectedAnimal

                elif x == self.starPin:
                    self.selectedAnimal = "star"
                    return self.selectedAnimal

                else:
                    print("Something went wrong. Please check the selected Pin")
                    return self.selectedAnimal
                    break

            else:
                pass



class LineSensor:

    def __init__(self, GPIO_LIGHT = 3, colorStop = 1):
        self.GPIO_LIGHT = GPIO_LIGHT # LineSensor GPIO pin
        self.colorStop = colorStop # returns 1 for black and 0 for WHITE
        self.pi = pigpio.pi()
        self.lineCrossed = False
    

    def levelChanged(self, gpio_num, level, tick):

        lineValue = self.pi.read(gpio_num)
        if (lineValue == self.colorStop):
            self.lineCrossed = True


    def runLineChecker(self):
        self.lineCrossed = False

        self.pi.set_mode(self.GPIO_LIGHT, pigpio.INPUT)
        cb = self.pi.callback(self.GPIO_LIGHT, pigpio.RISING_EDGE, self.levelChanged)
        
        while self.lineCrossed == False:
            time.sleep(0.5)
            print("Waiting for crossing Line.")

        print('Robot crossed line.')
        print('--------------------------------------------------------------------')
        time.sleep(2)
    