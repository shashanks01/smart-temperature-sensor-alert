import requests, json 
from datetime import datetime


def get_data(city):
    res = {}
    # Enter your API key here 
    api_key = "3e5f83554062eb8ca7241d3e8bee5808"
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    city_name = city 
    # city_name = "Bhatkal" 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    response = requests.get(complete_url) 
    x = response.json() 

    if x["cod"] != "404": 

        main = x["main"] 
        sys = x["sys"]
        wind = x["wind"]
        weather = x["weather"]  
        weather_description = weather[0]["description"] 

        res['feels_like'] = round(float(main["feels_like"])-273.15,2) 
        res['pressure'] = main["pressure"] 
        res['current_humidiy'] = main["humidity"] 
        res['sunrise'] = datetime.fromtimestamp(sys["sunrise"]).strftime('%Y-%m-%d %H:%M:%S')  
        res['sunset'] =  datetime.fromtimestamp(sys["sunset"]).strftime('%Y-%m-%d %H:%M:%S') 
        res['description'] = weather[0]["description"] 
        return res
    else: 
        print(" City Not Found ") 

# get_data("Bhatkal")