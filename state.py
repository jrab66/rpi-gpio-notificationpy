'''
Written by Jose Barahona
www.github.com/jrab66
February 02, 2016

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

'''

import RPi.GPIO as GPIO
import time
import os

#adjust for where your switch is connected Can be any GPIO.
buttonPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    #assuming the script to call is long enough we can ignore bouncing
    if (GPIO.input(buttonPin)):
        #this is the script that will be called (as root)
        os.system("python /root/emailgpio/emails.py")  #Directory change it for yours.
	GPIO.setup(buttonPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
