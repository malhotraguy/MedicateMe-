from twilio.rest import Client
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+15148349361",
    from_="+15146138562",
    body="You have an appointment tommorow. See you there")
