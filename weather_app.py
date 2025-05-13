# streamlit run weather_app.py

import streamlit as st
import os
import dotenv
from dotenv import load_dotenv
import requests
#import datetime
import time

load_dotenv()       # RECORDAR METER ESTO SIEMPRE!!! porque va a tomar el API_key de la cartella

API_key = os.getenv('api_key')

def obtain_data(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
    result = requests.get(url)
    json = result.json()

    return json

def weather_info(city_name):
    data = obtain_data(city_name)
    temp = round(data['main']['temp'] - 273.15,2)               # convertimos la tem a celcius--> - 273.15
    feelslike = round(data['main']['feels_like'] - 273.15,2)
    temp_min = round(data['main']['temp_min'] - 273.15,2)
    temp_max = round(data['main']['temp_max'] - 273.15,2)
    wind = round(data['wind']['speed'], 2)
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']
    output = [temp,feelslike,temp_min,temp_max,wind,sunrise,sunset]

    return  output

def to_datetime(float_data):
    hr = time.localtime(float_data).tm_hour
    min = time.localtime(float_data).tm_min

    return(f'{hr}:{min}')


def main():
    st.title('☔️ :rainbow[Weather Machine] ☔️')
    # st.subheader('...')
    #st.text('...')
    city_name = st.text_input("Città:")

    if st.button('🔍 Go!'):
        temp = weather_info(city_name)[0]
        feelslike = weather_info(city_name)[1]
        temp_min = weather_info(city_name)[2]
        temp_max = weather_info(city_name)[3]
        wind = weather_info(city_name)[4]
        sunrise = weather_info(city_name)[5]
        sunrise_time = to_datetime(sunrise)
        sunset = weather_info(city_name)[6]
        sunset_time = to_datetime(sunset)

        st.info('**Temperatura attuale (°C) =**' , temp,'°C')
        st.info('**Temperatura percepita (°C) =**' , feelslike,'°C')
        st.info('**Temperatura minima =**' , temp_min, '°C')
        st.info('**Temperatura massima =**' , temp_max, '°C')
        st.info('**Velocità del vento =**' , wind, 'm/s')
        st.info('**Alba =**' , sunrise_time)
        st.info('**Tramonto =** ' , sunset_time)


if __name__ == "__main__":
    main()


