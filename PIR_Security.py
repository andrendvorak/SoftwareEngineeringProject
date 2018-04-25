import RPi.GPIO as GPIO
import twilio
from twilio.rest import Client
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setip(13, GPIO.OUT)
account_sid = "" #Copy unique account sid here
auth_token = "" #Copy unique authentication token here

client = Client(account_sid, auth_token)

while True:
  i=GPIO.input(11)
  if i==0:
    print("No Activity", i)
    GPIO.output(13, False)
    time.sleep(1)
  elif i==1:
    print("Intruder", i)
    client.apt.account.messages.create(to="", from_="", body="MOTION DETECTED") #occupy to and from_ fields with your phone number and twilio number
    GPIO.output(13, True)
    time.sleep(5)
