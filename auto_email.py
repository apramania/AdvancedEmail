import smtplib
import os
from email.message import EmailMessage
import imghdr

EMAIL_ADDRESS = os.environ.get('Email_User')
EMAIL_PASSWORD = os.environ.get('Email_pass')

msg = EmailMessage()
msg['Subject'] = 'Meeting on 5th June'
msg['From'] = 'sender_email'
msg['To'] = 'reciever_email'
msg.set_content('To discuss various aspects of future propositions')

files = ['Linux-commands.pdf']
for file in files:
    with open(file, 'rb') as f:
        file_open = f.read()
        #file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_open, maintype = 'application', subtype = 'octet-stream', filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    #smtp.ehlo()
    #smtp.starttls()
    #smtp.ehlo()

    smtp.login('sender_email','password')

    #subject = 'Meeting on 5th June'
    #body = 'To discuss various aspects of future propositions'

    #msg = f'Subject: {subject}\n\n{body}'
    
    smtp.send_message(msg)


