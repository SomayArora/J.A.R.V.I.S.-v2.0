from twilio.rest import Client

# Your Twilio credentials
account_sid = ''  # Replace with your Account SID
auth_token = ''    # Replace with your Auth Token

client = Client(account_sid, auth_token)

# The number you're calling from (your Twilio number)
twilio_phone_number = ''  # Replace with your Twilio phone number

# The number you want to call
to_phone_number = ''  # Replace with the recipient's phone number

# Make a call
call = client.calls.create(
    to=to_phone_number,
    from_=twilio_phone_number,
    url='http://demo.twilio.com/docs/voice.xml'  # Twilio handles call instructions via URL
)

print(f"Call initiated. Call SID: {call.sid}")
