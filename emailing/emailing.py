import smtplib
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Mailing Client
server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
  password = f.read()

server.login('email', password)

# Message Description
msg = MIMEMultipart()
msg['From'] = 'Lubscript'
msg['To'] = 'testmails@spaml.de'
msg['Subject'] = 'Just A Test'

with open('message.txt', 'r') as f: 
  message = f.read()

msg.attach(MIMEText(message, 'plain'))

# Image Description
filename = 'here'
attachment = open(filename, 'rb')

# Payload object
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('sender', 'reciever', text)