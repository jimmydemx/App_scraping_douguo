from json import encoder
import requests
from parse import *
import data as info
import json 


url="http://api.douguo.net/recipe/flatcatalogs"

header_parse=multi_to_dic(info.header)

print("header_parse",header_parse)

data_parse=query_to_dic(info.data)
# order=r"weigh&operation=rent&propertyType=lands&locationId=0-EU-ES-48-01-001-020&maxItems=40&locationName=Bilbao%2CVizcaya&sort=desc&numPage=1&locale=es&quality=high&gallery=true"

r=requests.post(url,headers=header_parse,data=data_parse)

# print(r.text)

# from .json to dictionary in Python
# pat4 = 'get_list_fb\((.*)\);'
# results=re.compile(pat4).findall(r.text)
catalog = json.loads(r.text.encode("utf-8").decode("unicode_escape"))

print(catalog)