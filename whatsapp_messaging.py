from twilio.rest import Client
import json

def msg(event=None, context=None):

# get your sid and auth token from twilio and open it from saved txt files
# you probably do not want to share this information with everyone :)   

    with open('twilio_sid.txt', 'r') as f1:
        twilio_sid = f1.read()

    with open('auth_token.txt', 'r') as f2:
        auth_token = f2.read()

    with open('my_number.txt', 'r') as f3:
        my_number = f3.read()

    print(f"Configuration: sid {twilio_sid}, auth token {auth_token}, my number {my_number}")

    whatsapp_client = Client(twilio_sid, auth_token)

    # contact are saved in a json file
    with open('contacts.json') as contacts_json:
        contacts = json.load(contacts_json)
    print(f"Contacts is a dictionary {contacts}")


    for name, number in contacts.items():
        msg = whatsapp_client.messages.create(
                body = 'Good night {} !'.format(name),
                from_= 'whatsapp:' + my_number,
                to='whatsapp:' + number,

            )

        print(msg.sid)
msg()