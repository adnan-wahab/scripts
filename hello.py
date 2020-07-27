#from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

numbers = ['+1 281 305 1013', '+1 281 305 1550', '+1 281 305 1395', '+1 917 732 8538',
'+1 281 305 1262', '+1 281 305 1500', '+1 281 305 1635'

]

#app = Flask(__name__)
account_sid = 'AC03d4fbf8c20ecd86f31c9113956cc51c'
auth_token = 'e7f61acbfe558367f23b7a9f0f0f6085'
client = Client(account_sid, auth_token)


for n in numbers:
    message = client.messages.create(
                              body='daily reminder: people that abandon their friends are worse than trash',
                              from_=n,
                              to='+17136773669'
                          )

print(message.sid)
#
# @app.route('/bot', methods=['POST'])
# def bot():
#     incoming_msg = request.values.get('Body', '').lower()
#     resp = MessagingResponse()
#     msg = resp.message()
#     responded = False
#     if 'quote' in incoming_msg:
#         # return a quote
#         r = requests.get('https://api.quotable.io/random')
#         if r.status_code == 200:
#             data = r.json()
#             quote = f'{data["content"]} ({data["author"]})'
#         else:
#             quote = 'I could not retrieve a quote at this time, sorry.'
#         msg.body(quote)
#         responded = True
#     if 'cat' in incoming_msg:
#         # return a cat pic
#         msg.media('https://cataas.com/cat')
#         responded = True
#     if not responded:
#         msg.body('I only know about famous quotes and cats, sorry!')
#     return str(resp)
