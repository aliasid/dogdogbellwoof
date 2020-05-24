#!/usr/local/bin/python

# ddbw.py  aliasid, 2020-05-24

import sys
import time
import RPi.GPIO as GPIO
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER      = 'smtp.gmail.com' # Email server
SMTP_PORT        = 587              # Email server port for SMTP
PIN_TO_CIRCUIT   = 4                # the GPIO pin we use
MIN_MSG_SECS     = 60               # Minimum number seconds between sending msgs
SENSOR_THRESHOLD = 100000           # Min sensor reading to trigger msg

def send_msg():
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
		result = True
	except:
		result = False
	finally:
		return result

def rc_time ():
	count = 0

	# Output on the pin
	GPIO.setup( PIN_TO_CIRCUIT, GPIO.OUT)
	GPIO.output(PIN_TO_CIRCUIT, GPIO.LOW)
	time.sleep(0.1)

	# Change the pin back to input
	GPIO.setup( PIN_TO_CIRCUIT, GPIO.IN)

	# Count until the pin goes high
	while (GPIO.input(PIN_TO_CIRCUIT) == GPIO.LOW):
		count += 1

	return count

if __name__ == '__main__':

	prevtime = datetime(1970,1,1) # Initialize time of last msg send

	GPIO.setmode(GPIO.BCM)

	try:
		while True:
			reading = rc_time()
			curtime = datetime.now()
			output  = curtime.isoformat() + ': ' + str(reading)

			if reading >= SENSOR_THRESHOLD:
				output += '  Trigger!'

				if (curtime-prevtime).total_seconds() >= MIN_MSG_SECS:

					if send_msg():
						prevtime = curtime
						output  += '  Message sent.'
					else:
						output  += '  ERROR!'

			print(output)

	except KeyboardInterrupt:
		pass

	finally:
		GPIO.cleanup()
