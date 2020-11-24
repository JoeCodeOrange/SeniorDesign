#### Servo Test ####
# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
# GPIO.setup(19,GPIO.OUT)
# GPIO.setup(21,GPIO.OUT)
# GPIO.setup(29,GPIO.OUT)
# GPIO.setup(31,GPIO.OUT)
# GPIO.setup(33,GPIO.OUT)
# GPIO.setup(35,GPIO.OUT)
servo0 = GPIO.PWM(3,50) # Note 11 is pin, 50 = 50Hz pulse
servo1 = GPIO.PWM(5,50) # Note 13 is pin, 50 = 50Hz pulse
servo2 = GPIO.PWM(11,50) # Note 15 is pin, 50 = 50Hz pulse
servo3 = GPIO.PWM(13,50) # Note 17 is pin, 50 = 50Hz pulse
# servo4 = GPIO.PWM(19,50) # Note 15 is pin, 50 = 50Hz pulse
# servo5 = GPIO.PWM(21,50) # Note 17 is pin, 50 = 50Hz pulse
# servo6 = GPIO.PWM(29,50) # Note 15 is pin, 50 = 50Hz pulse
# servo7 = GPIO.PWM(31,50) # Note 17 is pin, 50 = 50Hz pulse
# servo8 = GPIO.PWM(33,50) # Note 15 is pin, 50 = 50Hz pulse
# servo9 = GPIO.PWM(35,50) # Note 17 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo0.start(0)
servo1.start(0)
servo2.start(0)
servo3.start(0)
# servo4.start(0)
# servo5.start(0)
# servo6.start(0)
# servo7.start(0)
# servo8.start(0)
# servo9.start(0)
print ("Waiting for 2 seconds")
time.sleep(2)


# Define variable duty
duty = 2


# Turn back to 90 degrees
print ("Turning back to 90 degrees for 2 seconds")
servo0.ChangeDutyCycle(7)
servo1.ChangeDutyCycle(7)
servo2.ChangeDutyCycle(7)
servo3.ChangeDutyCycle(7)
# servo4.ChangeDutyCycle(10)
# servo5.ChangeDutyCycle(10)
# servo6.ChangeDutyCycle(10)
# servo7.ChangeDutyCycle(10)
# servo8.ChangeDutyCycle(7)
# servo9.ChangeDutyCycle(7)
time.sleep(2)

#turn back to 0 degrees
print ("Turning back to 0 degrees")
servo0.ChangeDutyCycle(2)
servo1.ChangeDutyCycle(2)
servo2.ChangeDutyCycle(2)
servo3.ChangeDutyCycle(2)
# servo4.ChangeDutyCycle(2)
# servo5.ChangeDutyCycle(2)
# servo6.ChangeDutyCycle(2)
# servo7.ChangeDutyCycle(2)
# servo8.ChangeDutyCycle(2)
# servo9.ChangeDutyCycle(5)
time.sleep(0.5)
servo0.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
servo2.ChangeDutyCycle(0)
servo3.ChangeDutyCycle(0)
# servo4.ChangeDutyCycle(0)
# servo5.ChangeDutyCycle(0)
# servo6.ChangeDutyCycle(0)
# servo7.ChangeDutyCycle(0)
# servo8.ChangeDutyCycle(0)
# servo9.ChangeDutyCycle(0)

#Clean things up at the end
servo0.stop()
servo1.stop()
servo2.stop()
servo3.stop()
# servo4.stop()
# servo5.stop()
# servo6.stop()
# servo7.stop()
# servo8.stop()
# servo9.stop()
GPIO.cleanup()
print ("Goodbye")


## PINKY ##

## RING ##

## MIDDLE ##

## INDEX ##

## THUMB ##