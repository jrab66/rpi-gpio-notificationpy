rpi-gpio-notificationpy
====================

Written by Jose Barahona

February 02, 2016

This program is free software: you can redistribute it and/or modify it under the terms of the
 GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.


##use
you cant send email notifications when a GPIO has a change of state.

I use google server for the sending address for convenience, but you cant use
your prefered email server while this have SSL encryption (port 587).

state.py reads the status of the GPIO while emails.py sends a message when a change is detected.

you can add the line python /root/emailgpio/state.py to your  /etc/rc.local before exit 0 to execute the command at reboot without interaction.
