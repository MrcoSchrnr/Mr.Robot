import pigpio
import time


GPIO_IN1 = 5

pi = pigpio.pi()
#pi.set_mode(GPIO_IN1, pigpio.INPUT)

state = pi.read(GPIO_IN1)
state = str(state)
print(state)