 #This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager



flightSearch = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()


# adding in the iata codes
# for id in range (2,12):
#     city_name = data_manager.get_city(id)
#     city_code = flightSearch.get_city_code(city_name)
#     data_manager.set_city_code(city_code,id)
#
#
# #
for id in range(12):
        city_code = data_manager.get_city_code(id)
        lowest_flight_price = flightSearch.get_first_entry(city_code)["price"]
        current_lowest_price = data_manager.get_lowest_price(id)
        if lowest_flight_price < current_lowest_price:

            city_from = flightSearch.get_first_entry(city_code)["cityFrom"]
            aiport_from = flightSearch.get_first_entry(city_code)["flyFrom"]
            city_to = flightSearch.get_first_entry(city_code)["cityTo"]


            airport_to = flightSearch.get_first_entry(city_code)["flyTo"]
            date_from = flightSearch.get_first_entry(city_code)["route"][0]["local_departure"].split("T")[0]
            stopover_city = flightSearch.get_first_entry(city_code)["route"][0]["cityTo"]

            if stopover_city == city_to:
                notification_manager.send_user_message_no_stopover(city_from, aiport_from, city_to, airport_to, date_from,lowest_flight_price)
            else:
                notification_manager.send_user_message_stopover(city_from, aiport_from, city_to, airport_to, date_from,
                                                       lowest_flight_price,stopover_city)


