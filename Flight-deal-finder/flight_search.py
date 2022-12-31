from datetime import datetime,timedelta
import requests
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.tequila_api_key = "hC4hka3iH8z_7ssLMvwlV--E4K4B-hoa"
        self.api = "https://api.tequila.kiwi.com/locations/query"
        self.price_api = "https://api.tequila.kiwi.com/v2/search"
        self.headers = {
            "apikey": self.tequila_api_key
        }
        self.fly_from = "LON"

    def get_city_code(self,city):
        self.parameters = {
            "term": city

        }
        self.response = requests.get(url=self.api,params=self.parameters,headers=self.headers)
        self.data = self.response.json()['locations'][0]['code']
        return self.data

    def get_first_entry(self,destination_city_code):

        self.date_from = datetime.now().date()
        self.date_to = self.date_from + timedelta(days=180)

        #we will always check for the cheapest option so that we can compare quicker.
        try:
            paramters = {
                "date_from": self.date_from,
                "date_to": self.date_to,
                "fly_to": destination_city_code,
                "fly_from": self.fly_from,
                "max_stopovers": "0"
            }
            response = requests.get(url=self.price_api, params=paramters, headers=self.headers)
            data = response.json()["data"][0]
        except IndexError:
            paramters = {
                "date_from": self.date_from,
                "date_to": self.date_to,
                "fly_to": destination_city_code,
                "fly_from": self.fly_from,
                "max_stopovers": "1"
            }
            response = requests.get(url=self.price_api, params=paramters, headers=self.headers)
            data = response.json()["data"][0]

        return data

