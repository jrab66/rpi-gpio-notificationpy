import RPi.GPIO as GPIO
import time
import os

#adjust for where your switch is connected
buttonPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    #assuming the script to call is long enough we can ignore bouncing
    if (GPIO.input(buttonPin)):
        #this is the script that will be called (as root)
        os.system("python /root/emailgpio/emails.py")
	GPIO.setup(buttonPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
