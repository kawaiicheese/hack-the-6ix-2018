import twilio
from twilio.rest import Client
from KEYS import *

#The details for sending messages.
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN


client = Client(account_sid, auth_token)

def sendTo(phoneNumber, sender, receiver):
    message = client.messages.create(
        to="+16479093281", 
        from_="+16475034783",
        body="Hi! You have a notification from "+sender+".")

sendTo(1, "Suhavi", 2)
    