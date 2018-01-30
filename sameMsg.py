n=0
numbers=["+15148349361","+15143497155"]
for i in range(2):
    from twilio.rest import Client

    account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to=numbers[i],
        from_="+15146138562",
        body="Mister Peter, please do not forget your tomorrow's appointment at 10:00AM")
