import requests
from bs4 import BeautifulSoup
import fake_useragent
from random import *




list_link = ["https://www.fitnessbar.ru/catalog/action-nutrition-bolt-extreme-energy-232-g/",
"https://www.fitnessbar.ru/catalog/action-nutrition-bolt-extreme-energy-232-g/",
"https://www.fitnessbar.ru/catalog/action-nutrition-bolt-extreme-energy-232-g/",
"https://www.fitnessbar.ru/catalog/action-nutrition-bolt-extreme-energy-232-g/",
"https://www.fitnessbar.ru/catalog/afn-creaton-300-g/", "https://www.fitnessbar.ru/catalog/afn-glutamine-isc-300-g/",
"https://www.fitnessbar.ru/catalog/afn-guarana-3200-ml/",
"https://www.fitnessbar.ru/catalog/afn-guarana-3200-ml/",
"https://www.fitnessbar.ru/catalog/afn-guarana-3200-ml/",
"https://www.fitnessbar.ru/catalog/afn-zma-90-caps/",
"https://www.fitnessbar.ru/catalog/afn-bcaa-7500-300-g/",
"https://www.fitnessbar.ru/catalog/maxler-bcaa-8400-360-tabletok/",
"https://www.fitnessbar.ru/catalog/bsn-amino_x/",
"https://www.fitnessbar.ru/catalog/universal-nutrition-animal-flex-30-paketikov/",
"https://www.fitnessbar.ru/catalog/universal-nutrition-animal-pak-30-paketikov/"]




user = fake_useragent.UserAgent().random
header = {
    "user-agent": user
}


url = "https://www.fitnessbar.ru/catalog/maxler-bcaa-8400-360-tabletok/"

for link in list_link:
    responce = requests.get(url=link, headers=header).text
    soup = BeautifulSoup(responce, "lxml")

    condition = soup.find(class_="b-p-t-inner__name").text
    if condition.strip() == "Нет в наличии":
        print("Товар отсутствует")
    else:
        price = soup.find(class_="b-price__normal").text
        print(price.strip())
        print(condition.strip())




