import urllib.request
import json

def api(my_api):
    print('Enter latitude:')
    lat = input()
    print('Enter longtitude:')
    lon=input()
    url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units=metric&exclude=minutely,current,hourly,alerts&appid={}".format(lat, lon, my_api)
    json_obj = urllib.request.urlopen(url)
    data = json.load(json_obj)
    x=0
    for i in data['daily'][:6]:
        print('day', x,'. Morn:', i['temp']['morn'],'; Max:',i['temp']['max'])
        x+=1
api(my_api)