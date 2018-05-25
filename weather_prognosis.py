import requests
import argparse


def get__city_id(s_city, app_id):
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                       params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': app_id})
    data = res.json()
    city_id = data['list'][0]['id']
    return city_id


def get_weather_for_five_days(city_id, app_id):
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
    return res.text


parser = argparse.ArgumentParser(description = 'получение прогноза погоды с сайта "http://api.openweathermap.org/"')
parser.add_argument("--city", help = 'Город (название на английском)', default = "Moscow")
parser.add_argument("--app_id", help = 'id из личного кабинета на сайте')
args = parser.parse_args()


app_id = args.app_id
city = args.city
corpus = 'json_dictionery.json'

city_id = get__city_id(city, app_id)
D = get_weather_for_five_days(city_id, app_id)
with open(corpus, 'w',  encoding="utf-8") as fout:
    print(D, file = fout)
