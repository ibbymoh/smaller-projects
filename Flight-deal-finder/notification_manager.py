
from  twilio.rest import Client
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = "AC7e0f277ef5f6bc3e469f5f71dae08851"
        self.auth_token = "8e3937514ff733ceffd2f4d72db71a96"
        self.from_number = "+16812022991"
        self.to_number = "+201097834536"
        self.client = Client(self.account_sid, self.auth_token)



    def send_user_message_no_stopover(self,city_from,aiport_from ,city_to,airport_to,date_from,lowest_flight_price):
        message = self.client.messages.create(
            body=f"NEW flight deal! £{lowest_flight_price} from {city_from}-{aiport_from} to {city_to}-{airport_to} on {date_from}",
            from_=self.from_number,
            to=self.to_number
        )

    def send_user_message_stopover(self, city_from, airport_from, city_to, airport_to, date_from,
                                      lowest_flight_price,stopover_city):
        message = self.client.messages.create(
            body=f"NEW flight deal! £{lowest_flight_price} from {city_from}-{airport_from} to {city_to}-{airport_to} on {date_from}\n The flight has one stopover in {stopover_city}",
            from_=self.from_number,
            to=self.to_number
        )


