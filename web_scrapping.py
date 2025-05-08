from bs4 import BeautifulSoup

import requests

url = "https://viisipennia.fi/lounas/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify())

prices = doc.find_all(string="G")
print(prices)
