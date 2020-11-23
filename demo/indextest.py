#### Servo Test ####
# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse
servo2 = GPIO.PWM(13,50) # Note 13 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
servo2.start(0)
print ("Waiting for 2 seconds")
time.sleep(2)


# Define variable duty
duty = 2


# Turn back to 90 degrees
print ("Turning back to 90 degrees for 2 seconds")
servo1.ChangeDutyCycle(7)
servo2.ChangeDutyCycle(7)
time.sleep(2)

#turn back to 0 degrees
print ("Turning back to 0 degrees")
servo1.ChangeDutyCycle(2)
servo2.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
servo2.ChangeDutyCycle(0)

#Clean things up at the end
servo1.stop()
servo2.stop()
GPIO.cleanup()
print ("Goodbye")


## PINKY ##

## RING ##

## MIDDLE ##

## INDEX ##

## THUMB ##