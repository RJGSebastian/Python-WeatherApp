import tkinter as tk

import requests

canv_height = 360
canv_width = 480
div_l = 16


# c05e02789078b9cfd9371da5df92a99d
# api.openweathermap.org/data/2.5/weather?q={city name},{country code}


def format_response(weather):
    try:
        name = weather['name']
        country = weather['sys']['country']
        curr_weather = weather['weather'][0]['description']
        cloudiness = weather['clouds']['all']
        curr_temp = weather['main']['temp']
        temp_min = weather['main']['temp_min']
        temp_max = weather['main']['temp_max']
        pressure = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']

        final_output = f"""Current Weather in {name}, {country}: \nWeather: {curr_weather}, Cloudiness: {cloudiness}% 
        \nTemperature: {curr_temp}°C ({temp_min}°C - {temp_max}°C) \nPressure: {pressure}hPa \nHumidity: {humidity}% 
        \nWind speed: {wind_speed}m/s """

        print("*" * div_l)
        print(final_output)
    except:
        final_output = "There was a problem retrieving this information"

    return final_output


def get_weather(city):
    print("*" * div_l)
    print(f"Searching for weather in {city}.")
    weather_key = 'c05e02789078b9cfd9371da5df92a99d'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    print(response.json())

    weather = response.json()
    l_weather_result['text'] = format_response(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height=canv_height, width=canv_width)
background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
canvas.pack()

upper_frame = tk.Frame(root, bg='#4d94ff')
upper_frame.place(anchor='n', relx=0.5, rely=0.1, relwidth=0.8, relheight=0.2)

lower_frame = tk.Frame(root, bg='#4d94ff')
lower_frame.place(anchor='n', relx=0.5, rely=0.3, relwidth=0.8, relheight=0.6)

l_entry = tk.Label(upper_frame, text="City, Country:", font=('Calibri', 14))
l_entry.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.4)

e_city = tk.Entry(upper_frame, font=('Calibri', 12))
e_city.place(relx=0.05, rely=0.55, relwidth=0.55, relheight=0.4)

b_get_weather = tk.Button(upper_frame, text="Search", command=lambda: get_weather(e_city.get()), font=('Calibri', 12))
b_get_weather.place(relx=0.65, rely=0.55, relwidth=0.3, relheight=0.4)

l_weather_result = tk.Label(lower_frame, font=('Calibri', 12), anchor='nw', justify='left', bd=4)
l_weather_result.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

root.mainloop()
