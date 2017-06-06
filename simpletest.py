# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
#servo_min = 150  # Min pulse length out of 4096
#servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
#while True:
    # Move servo on channel O between extremes.
	
#init
def	init():
	pwm.set_pwm(0, 0, 360)
	pwm.set_pwm(1, 0, 360)
	pwm.set_pwm(2, 0, 360)
	pwm.set_pwm(12, 0, 360)
	pwm.set_pwm(4, 0, 360)
	pwm.set_pwm(5, 0, 300)
	pwm.set_pwm(6, 0, 360)
	pwm.set_pwm(7, 0, 150)
	pwm.set_pwm(8, 0, 360)
	pwm.set_pwm(9, 0, 360)
	pwm.set_pwm(10, 0, 360)
	pwm.set_pwm(11, 0, 360)
	time.sleep(1)
#up	
def up():
	for i in range(1,10,1):
		pwm.set_pwm(1, 0, 360+15*i+5)
		pwm.set_pwm(4, 0, 360-15*i)
		pwm.set_pwm(7, 0, 150+15*i)
		pwm.set_pwm(10, 0, 360-15*i)
		pwm.set_pwm(0, 0, 360+15*i-5)
		pwm.set_pwm(12, 0, 360-15*i)
		pwm.set_pwm(6, 0, 360+15*i)
		pwm.set_pwm(9, 0, 360-15*i)
		time.sleep(0.2)
	time.sleep(2)
#left
def left():
	pwm.set_pwm(5, 0, 420)
	time.sleep(0.5)
	pwm.set_pwm(12, 0, 360)
	pwm.set_pwm(4, 0, 360)
	pwm.set_pwm(9, 0, 360)
	pwm.set_pwm(10, 0, 360)
	pwm.set_pwm(2, 0, 240)
	pwm.set_pwm(8, 0, 240)
	pwm.set_pwm(11, 0, 480)
	time.sleep(0.5)
	pwm.set_pwm(5, 0, 300)
	pwm.set_pwm(4, 0, 420)
	pwm.set_pwm(12, 0, 330)
	time.sleep(0.5)
	pwm.set_pwm(9, 0, 240)
	pwm.set_pwm(10 , 0, 240)
	time.sleep(0.5)

#right
def right():
	pwm.set_pwm(2, 0, 240)
	time.sleep(0.5)
	pwm.set_pwm(1, 0, 360)
	pwm.set_pwm(0, 0, 360)
	pwm.set_pwm(6, 0, 360)
	pwm.set_pwm(7, 0, 150)
	pwm.set_pwm(5, 0, 420)
	pwm.set_pwm(8, 0, 240)
	pwm.set_pwm(11, 0, 480)
	time.sleep(0.5)
	pwm.set_pwm(2, 0, 390)
	pwm.set_pwm(1, 0, 300)
	pwm.set_pwm(0, 0, 390)
	time.sleep(0.5)
	pwm.set_pwm(6, 0, 480)
	pwm.set_pwm(7 , 0, 270)
	time.sleep(0.5)
#forward
def forward():
	pwm.set_pwm(2, 0, 240)
	pwm.set_pwm(5, 0, 420)
	pwm.set_pwm(8, 0, 240)
	pwm.set_pwm(11, 0, 480)
	pwm.set_pwm(0, 0, 360)
	pwm.set_pwm(1, 0, 360)
	pwm.set_pwm(6, 0, 360)
	pwm.set_pwm(7, 0, 150)
	time.sleep(0.5)
	pwm.set_pwm(0, 0, 480)
	pwm.set_pwm(1, 0, 300)
	time.sleep(0.5)
	pwm.set_pwm(6, 0, 480)
	pwm.set_pwm(7, 0, 270)
	time.sleep(0.5)
	pwm.set_pwm(0, 0, 360)
	pwm.set_pwm(1, 0, 360)
	time.sleep(0.5)
	pwm.set_pwm(6, 0, 360)
	pwm.set_pwm(7, 0, 150)
	time.sleep(0.5)

	pwm.set_pwm(12, 0, 240)
	pwm.set_pwm(4, 0, 420)
	time.sleep(0.5)
	pwm.set_pwm(9, 0, 240)
	pwm.set_pwm(10, 0, 240)
	time.sleep(0.5)
	pwm.set_pwm(12, 0, 360)
	pwm.set_pwm(4, 0, 360)
	time.sleep(0.5)
	pwm.set_pwm(9, 0, 360)
	pwm.set_pwm(10, 0, 360)

def ini2():
	pwm.set_pwm(2, 0, 240)
	pwm.set_pwm(5, 0, 420)
	pwm.set_pwm(8, 0, 240)
	pwm.set_pwm(11, 0, 480)
	pwm.set_pwm(0, 0, 360)
	pwm.set_pwm(1, 0, 360)
	pwm.set_pwm(12, 0, 360)
	pwm.set_pwm(4, 0, 360)
	pwm.set_pwm(6, 0, 360)
	pwm.set_pwm(7, 0, 150)
	pwm.set_pwm(9, 0, 360)
	pwm.set_pwm(10, 0, 360)


def ini3():
	#pwm.set_pwm(2, 0, 240)
	pwm.set_pwm(5, 0, 420)
	pwm.set_pwm(8, 0, 240)
	pwm.set_pwm(11, 0, 480)
	#pwm.set_pwm(0, 0, 360)
	#pwm.set_pwm(1, 0, 360)
	#pwm.set_pwm(12, 0, 360)
	pwm.set_pwm(4, 0, 360)
	pwm.set_pwm(6, 0, 360)
	pwm.set_pwm(7, 0, 150)
	pwm.set_pwm(9, 0, 360)
	pwm.set_pwm(10, 0, 360)

#while True:
#	ini2()
#	ini3()
#	pwm.set_pwm(13, 0, 360)
#	time.sleep(1)	
