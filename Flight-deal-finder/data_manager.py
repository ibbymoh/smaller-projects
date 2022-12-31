import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_api_url = "https://api.sheety.co/ba916a6f42426c154b377b0a61f27aa2/copyOfFlightDeals/prices"



    def get_city(self,id):
        self.response = requests.get(url=f"{self.sheety_api_url}/{id}")
        self.data = self.response.json()["price"]["city"]
        return self.data

    def get_lowest_price (self,id):
        self.response = requests.get(url=f"{self.sheety_api_url}/{id}")
        self.data = self.response.json()["price"]["lowestPrice"]
        return self.data

    def get_city_code(self,id):
        self.response = requests.get(url=f"{self.sheety_api_url}/{id}")
        self.data = self.response.json()["price"]["iataCode"]
        return self.data



    def set_city_code(self,code,id):

      parameters =  {
          "price": {
              "iataCode": f"{code}"
          }
      }


      self.response = requests.put(url=f"{self.sheety_api_url}/{id}",json=parameters)