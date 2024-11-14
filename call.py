from twilio.rest import Client

# Your Twilio credentials
account_sid = 'AC346d1936c7a9d988d1bc0d17b68bb767'  # Replace with your Account SID
auth_token = '2bfd4c10b51343447a598dca9cd71c34'    # Replace with your Auth Token

client = Client(account_sid, auth_token)

# The number you're calling from (your Twilio number)
twilio_phone_number = '+17756004110'  # Replace with your Twilio phone number

# The number you want to call
to_phone_number = '+919289058038'  # Replace with the recipient's phone number

# Make a call
call = client.calls.create(
    to=to_phone_number,
    from_=twilio_phone_number,
    url='http://demo.twilio.com/docs/voice.xml'  # Twilio handles call instructions via URL
)

print(f"Call initiated. Call SID: {call.sid}")
