# import requests
# import re
#
#
# reg_property_history_row = re.compile('propertyHistory\-[0-9]+')
# reg_property_urls = re.compile('(/[A-Z][A-Z]/[A-Za-z\-/0-9]+/home/[0-9]+)')
#
# class Redfin():
#     def __init__(self):
#         self.start_url = 'https://www.redfin.com/'
#         self.city_info = "city/30802/TX/Pflugerville/"
#
#     def get_all_listings(self):
#         response = requests.get(self.start_url + self.city_info)
#         return reg_property_urls.findall(response.text.replace('\\u002F', '/'))
#
#     def get_listing_info(self, url_partial):
#         response = requests.get(self.start_url + url_partial.replace(self.city_info, ""))
#         return reg_property_history_row.findall(response.text.replace('\\u002F', '/'))
#
# redfin = Redfin()
# houses = redfin.get_all_listings()
# print(houses)
# for house in houses:
#     print(redfin.get_listing_info(house))
#
#

import redfin
from bson import json_util
import json

client = redfin.RedFin()
# results = client.get_search_results()
# print(results)

data = client.get_property_data(["/TX/Austin/6317-Graymont-Dr-78754/home/146112273"])


print(json.dumps(data))