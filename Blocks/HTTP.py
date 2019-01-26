import csv
import json
import requests 
URL = "https://api.mercadolibre.com/"
withNick="sites/MLA/search?nickname="
Nick="candy-ho"
req=  URL+withNick+Nick #forms the API endpoint
test= requests.get(req) #test is a requests.model.response. The JSON is in the text field
data= json.loads(test.text) #parses the response.text
