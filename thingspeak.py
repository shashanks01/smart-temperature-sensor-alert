import requests, json
from datetime import datetime, timedelta

#"https://api.thingspeak.com/channels/1101830/feeds.json?api_key=SYSOFLYNTJS3O12R&results=2&start=2020-07-19%2008:38:58&end=2020-07-19%2008:38:58"
base_url = "https://api.thingspeak.com/channels/1101830/feeds.json?api_key=SYSOFLYNTJS3O12R&results=1"


def get_summary(date_time_now, temperature, humidity):
    # Forming the summary
    rainy = [6, 7, 8, 9, 10, 11]
    summer = [12, 1, 2, 3, 4]
    text = ""
    month = date_time_now.month

    if month in rainy:
        text += "This is Rainy season, Preferred crops - paddy, sugercane. "

        if(float(temperature) > 30):
            text += "temperature is above 30. "
        else:
            text += "temperature is below 30. "

        if(float(humidity) > 80):
            text += "humidity above 80."
        else:
            text += ""

    elif month in summer:
        if(int(temperature) > 33):
            text += ""
        else:
            text += ""
    else:
        text += "This is the month of May, Expecting monsoon in a few weeks."

    return text

def get_thingspeak_data():
    # getting data of current time from things speak
    date_time_now = datetime.now() 
    end = date_time_now.strftime("%Y-%m-%d %H:%M:%S").split(' ')
    start = (date_time_now - timedelta(hours=15, minutes=2)).strftime("%Y-%m-%d %H:%M:%S").split(' ')

    url = base_url + "start=" + start[0] + "%20" + start[1] + "&end=" + end[0] + "%20" + end[1]

    response = requests.get(url) 
    data = response.json()

    # extracting temperature and humidity from the data
    temperature = data['feeds'][0]['field1']
    humidity = data['feeds'][0]['field2'].rstrip()

    summary = get_summary(date_time_now, temperature, humidity)

    result = {'temperature': temperature, 'humidity': humidity, 'text': summary}
    return result

# get_thingspeak_data()