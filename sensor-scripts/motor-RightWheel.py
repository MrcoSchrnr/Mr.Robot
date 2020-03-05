import pigpio
import time

# @pre pigpio demon must be running (sudo pigpiod)
# Hardware PWM available for GPIO 12, 13, 18, 19 (BCM scheme)

GPIO_PWM = 12 # PWM pin
GPIO_IN1 = 23 # motor control pin
GPIO_IN2 = 24 # motor control pin

pi = pigpio.pi()

# Motor control pins
# 0, 1 forward (whatever that means in your case)
# 1, 0 reverse
# 1, 1 brake
# 0, 0 stop slowly

def drive(ahead = True, frequency = 50000, duty_cycle = 10):

    PWM_FREQUENCY = frequency #Hz
    PWM_DUTY_CYCLE = duty_cycle #percent

    if ahead == True:
        pi.set_mode(GPIO_IN1, pigpio.OUTPUT)
        pi.set_mode(GPIO_IN2, pigpio.OUTPUT)
        pi.write(GPIO_IN1, 1)
        pi.write(GPIO_IN2, 0)

    elif ahead == False:
        pi.set_mode(GPIO_IN1, pigpio.OUTPUT)
        pi.set_mode(GPIO_IN2, pigpio.OUTPUT)
        pi.write(GPIO_IN1, 0)
        pi.write(GPIO_IN2, 1)

    try:
        duty = PWM_DUTY_CYCLE * 10000 # Max: 1M
        pi.hardware_PWM (GPIO_PWM, PWM_FREQUENCY, duty)
        print('Hardware PWM on GPIO ' + str(GPIO_PWM) + ' enabled')
        print('Frequency: ' + str(pi.get_PWM_frequency(GPIO_PWM)) + ' Hz')
        print('Dutycycle: ' + \
              str(pi.get_PWM_dutycycle(GPIO_PWM) / 10000) + ' percent')

    except: 
        print('Hardware PWM not available on GPIO ' + str(GPIO_PWM))
        pi.stop()

def stop():
    pi.set_mode(GPIO_IN1, pigpio.OUTPUT)
    pi.set_mode(GPIO_IN2, pigpio.OUTPUT)
    pi.write(GPIO_IN1, 1)
    pi.write(GPIO_IN2, 1)

def shutDown():
    #disable PWM
    pi.write(GPIO_PWM, 0)

    # Free resources
    pi.stop()

def test():
    drive(True, frequency=50000, duty_cycle=50)
    time.sleep(5)
    stop()
    shutDown()

test()