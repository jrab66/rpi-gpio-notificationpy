# -*- coding: utf-8 -*--

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


import smtplib

#mime import email modules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#email addresses
#recipients
addr_to = 'xxxxxx@xxxx.com'
#end recipients
addr_from = 'xxxxxx@gmail.com' #my email
#SMTP server details
smtp_server = 'smtp.gmail.com' #smtp server in this case i use gmail
smtp_user = 'xxxxxx@gmail.com' #email
smtp_pass = 'password' #email password


#Connection Server
server = smtplib.SMTP(smtp_server,587)
server.ehlo()
server.starttls()
server.login(smtp_user,smtp_pass)
#msg config
msg = MIMEMultipart('alternative')
msg['To'] = addr_to
msg['From'] = addr_from
msg['Subject'] = 'Alarm! GPIO State'

#html version
text = "Test email GPIO state"
html = """\
<html>
	<head> <meta charset="UTF-8"></head>
	<body>
	  <p>Test email GPIO state</p>
	</body>
</html>
"""

#parsing  msg email
part1 = MIMEText(text,'plain')
part2 = MIMEText(html,'html')
msg.attach(part1)
msg.attach(part2)

#sending email
server.sendmail(addr_from, addr_to, msg.as_string())
server.quit()
