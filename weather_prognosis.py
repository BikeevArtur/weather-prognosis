import requests


def get__city_id(s_city, app_id):
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                       params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': app_id})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    city_id = data['list'][0]['id']
    return city_id


def get_weather(city_id, app_id):
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
    data = res.json()
    return data


def get_weather_for_five_days(city_id, app_id):
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
    return res.text


app_id = "7edfb557af094b5492ed89f7e07ec190"
city = "London"
corpus = 'json_dictionery'

city_id = get__city_id(city, app_id)
D = get_weather_for_five_days(city_id, app_id)
with open(corpus, 'w',  encoding="utf-8") as fout:
    print(D, file = fout)