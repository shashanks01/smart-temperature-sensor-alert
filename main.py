import requests, weather, json, thingspeak

'''
    This is the main module. This fetches the data from things speak and openweathermap and sends the sms using fast2sms.
'''


url = "https://www.fast2sms.com/dev/bulk"

users = None

with open("D:\\Code\\Demo\\userdata.csv", 'r') as f:
    users = f.readlines()

numbers = ""

for user in users:
    userdata = user.split(",") 
    name = userdata[0] 
    city = userdata[1] 
    phone = userdata[2]

    # get data from weather and thinsspeak
    data = weather.get_data(city)
    summary = thingspeak.get_thingspeak_data()

    # print(summary)
    # print(data)

    # from the msg and place the data at appropriate position.
    display_data = "\n\n Hello {name}, today's temperature in {city} is at {temp} degree Celcius and it feels like {feels_like}. " \
                        "Humidity at your field reads {humidity} and Pressure is at {pressure}. Current weather description is {description}." \
                        " {summary}".format(name= name, city = city, temp = summary['temperature'], feels_like = data['feels_like'], 
                        humidity = summary['humidity'], pressure = data['pressure'], description = data['description'], summary = summary['text'])

    print(display_data)

    #Balachandra,Bhatkal,6360239412

    # This is the payload data to be posted to the messaging application
    payload = """sender_id=FSTSMS&message={display_data}&language=english&route=p&numbers={phone}""".format(display_data=display_data, phone=phone)

    headers = {
    'authorization': "jpowiyhN0kXqYDgZWbzMtUQ9cu4KT32avnIO8exGPmRrsESfFVN2jKHwPuxqmQbUIkWTadGcDehnfr5Y",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

    # Sending message
    # response = requests.request("POST", url, data=payload, headers=headers)
    # print(response.text)