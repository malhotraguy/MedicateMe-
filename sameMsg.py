n=0
numbers=["+15148349361","+15143497155"]
for i in range(2):
    from twilio.rest import Client

    account_sid = "ACddc59696c52e6d717778a4621d700dc1"
    auth_token = "c324cdc7ba3923cb9b832d7f9975427a"

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to=numbers[i],
        from_="+15146138562",
        body="Mister Peter, please do not forget your tomorrow's appointment at 10:00AM")
