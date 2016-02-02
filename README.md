rpi-gpio-notificationpy
====================

Written by Jose Barahona
www.github.com/jrab66
February 02, 2016

This program is free software: you can redistribute it and/or modify it under the terms of the
 GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

##use
====================

you cant send email notifications when a GPIO has a change of state.

I use google server for the sending address for convenience, but you cant use
your prefered email server while this have SSL encryption (port 587).

state.py reads the status of the GPIO while emails.py sends a message when a change is detected.

you can add the line to /etc/rc.local to execute the command at reboot without interaction.

Example :
`code(fffffffff sdfsdf)`
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

#rpi-gpio-notificationpy python script
python /root/emailgpio/state.py

exit 0
`code()`
