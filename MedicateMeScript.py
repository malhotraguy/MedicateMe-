# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client
#! curl https://raw.githubusercontent.com/malhotraguy/Patient_data/master/database.json -o patient_database.json
import json


def create_individual_file():
    with open('patient_database.json') as patient_database_file:
        data = json.load(patient_database_file)
        print(data)
        for p in data["Patient"]:
            print("p=", p)
            nf = open(p['ID'] + " " + p['name'] + ".txt", 'w+')
            for ep in p:
                print(ep, "=", p[ep])
                # change=input("Do you want to change:(Y): ")
                # if change.upper()=="Y":
                # new_val=input("Enter new value: ")
                # ep=new_val
                # else:
                # pass
                # for p in data['Patient']:
                # for ep in p:
                # print("New Data\n")
                # print(ep,"=",p[ep])

            nf.write(
                p['ID'] + " " + p['name'] + " " + p['medicine'] + " " + p['frequency'] + " " + p['duration'] + " " + p[
                    'appointment'] + " " + p['remarks'] + "\n")
            nf.close()
    patient_database_file.close()


create_individual_file()
text_name=input("Enter the name of person to sent alert: ")
text_id=input("Enter the id of the patient: ")
text_file=open(text_id+" "+text_name+".txt",'r+')
text_data=text_file.read()


# Find these values at https://twilio.com/user/account
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+15148349361",
    from_="+15146138562",
    body=text_data)
