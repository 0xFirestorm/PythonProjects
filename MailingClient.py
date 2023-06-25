import re
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

regex = ".+@gmail.com"
print(" SIMPLE EMAIL CLIENT ")
while True:
    emailadd = input("Enter your gmail address: ")
    if(not re.fullmatch(regex,emailadd)):
        print("Invalid email format")
    else:
        break
passw = getpass("Enter your password: ")

server = smtplib.SMTP('smtp.gmail.com', 587)

# start the service
server.ehlo()
# starting up the connection
server.starttls()

# logging into our account
try:
    server.login(emailadd, passw)
except Exception as msg:
    print(msg)
    sys.exit(1)

msg = MIMEMultipart()
em_from = input("From: ")
em_to = input("To: ")
em_subject = input("Subject: ")
em_message = input("Message: ")
msg['From'] = em_from
msg['To'] = em_to
msg['Subject'] = em_subject
message = em_message
msg.attach(MIMEText(message, 'plain'))
text = msg.as_string()
server.sendmail(emailadd, em_to,text)
print("Email Sent!")
