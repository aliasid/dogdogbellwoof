# ddbw.py  aliasid, 2020-05-24

import sys
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER =  'smtp.gmail.com'
SMTP_PORT   =  587

if __name__ == '__main__':
    sender_address   = sys.argv[1]
    sender_pass      = sys.argv[2]
    receiver_address = sys.argv[3]
    
    message = MIMEMultipart()
    message['From']    = sender_address
    message['To']      = receiver_address
    message['Subject'] = 'dogdogbell'   
    message.attach(MIMEText('Woof!','plain'))
    
    try:
        session = smtplib.SMTP(SMTP_SERVER,SMTP_PORT) 
        session.starttls() # enable security
        session.login(sender_address,sender_pass) # login with mail_id and password
        session.sendmail(sender_address,receiver_address,message.as_string())
        session.quit()
        result = 'msg sent'
    except:
        result = 'error'
    finally:
        print(time.strftime('%FT%T')+': '+result)
