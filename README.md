Graphic weather analitic
============================

## weather-prognosis

Получает прогноз погоды на ближайшие 5 дней по часам с [сайта погоды](http://api.openweathermap.org), приводит словарь с данными в строковый формат, загружает в файл `'json_dictionery'`

Получает на вход аргументы:

    --app_id(id с сайта),
    --city(необязательный, по дефолту Moscow)

Получает словарь с данными о погоде на каждые три часа в ближайшие 5 суток(40 замерений), выводит в файл.
Пример:

    Users...\python.exe weather-prognosis.py --city London --app_id 7...0
***
## weather-analisys

Загружает словарь из из `'json_dictionery'` в виде строки, парсит его с помощью json.loads; Выводит график зависимости температуры от времени.

#### Пример № 1: график перепада температур в Лондоне в течении 5 суток


![Alt text](https://github.com/BikeevArtur/weather-prognosis/blob/master/Figure_0.png?raw=true "Optional Title")


Затем (после закрытия окна с графиком) выводит круговую гистограмму с типами погоды: "пасмурно", "дождь"... в процентном соотношении.
#### Пример № 2: диаграмма изменения погоды в Лондоне


![Alt text](https://github.com/BikeevArtur/weather-prognosis/blob/master/Figure_1.png?raw=true "Optional Title")
