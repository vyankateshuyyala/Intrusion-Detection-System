from twilio.rest import Client
account_sid = 'account_id'
auth_token = 'auth_token'
client = Client(account_sid, auth_token)
def sendSms():
    message = client.messages.create(
    from_='+910000000000',
    body='Alert ',
    to='+910000000000'
    )

    print(message.sid)
