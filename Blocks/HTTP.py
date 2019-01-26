import csv
import json
import requests 
URL = "https://api.mercadolibre.com/"
withNick="sites/MLA/search?nickname="
Nick="candy-ho"
req=  URL+withNick+Nick 
print(req)
test= requests.get(req)
print(test)
