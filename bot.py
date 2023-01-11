from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'somosree' in incoming_msg:
        msg.body('Hi Beautiful, How can I help you? Your name is somosree right?')
    return str(resp)


if __name__ == '__main__':
    app.run(port=4000)