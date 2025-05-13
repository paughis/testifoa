# streamlit run weather_app.py

import streamlit as st
import pandas as pd
# import os (solo locale!)
import requests
import time

#### solo locale:
# from dotenv import load_dotenv
# load_dotenv()       # RECORDAR METER ESTO SIEMPRE!!! porque va a tomar el API_key de la cartella
# API_key = os.getenv('api_key')

#### secrets per stremalit.io:
# secrets in api_key in stringa api_key = "xxxxxxxxxxxxxxxxxxxxxxxx"
API_key = st.secrets['api_key']

def obtain_data(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
    result = requests.get(url)
    #json = result.json()
    return result

def weather_info(data):
    #data = obtain_data(city_name)
    temp = round(data['main']['temp'] - 273.15,2)               # convertimos la tem a celcius--> - 273.15
    feelslike = round(data['main']['feels_like'] - 273.15,2)
    temp_min = round(data['main']['temp_min'] - 273.15,2)
    temp_max = round(data['main']['temp_max'] - 273.15,2)
    wind = round(data['wind']['speed'], 2)
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']
    lat = data['coord']['lat']
    lon = data['coord']['lon']
    output = [temp,feelslike,temp_min,temp_max,wind,sunrise,sunset,lat,lon]

    return  output

def to_datetime(float_data):
    hr = time.localtime(float_data).tm_hour
    min = time.localtime(float_data).tm_min

    return(f'{hr}:{min}')


def main():
    st.title('☔️ :rainbow[Weather Machine] ☔️')

    city_name = st.text_input("Città:")
    
    col1, col2 = st.columns(2)
    if st.button('🔍 Go!'):

        # checkeamos si esta en blanco
        if not city_name.strip():
            st.error('⚠️ Inserire il nome di una città!')
            return
        
    response = obtain_data(city_name)

    # checkeamos que la ciudad exista en la API
    if response.status_code != 200:
        st.error(f'⚠️ Oops, impossibile trovare la città "{city_name}". Controlla ortografia e riprova')
        return
    
    data = response.json()
    weather_data = weather_info(data)

    with col1:
        temp = weather_data[0]
        feelslike = weather_data[1]
        temp_min = weather_data[2]
        temp_max = weather_data[3]
        wind = weather_data[4]
        sunrise = weather_data[5]
        sunrise_time = to_datetime(sunrise)
        sunset = weather_data[6]
        sunset_time = to_datetime(sunset)

        st.info(f'**Temperatura attuale** ➡️ {temp}°C')
        st.info(f'**Temperatura percepita** ➡️ {feelslike}°C')
        st.info(f'**Temperatura minima** ➡️ {temp_min}°C')
        st.info(f'**Temperatura massima** ➡️ {temp_max} °C')
        st.info(f'**Velocità del vento** ➡️ {wind} m/s')
        st.info(f'**Alba** ➡️ {sunrise_time}')
        st.info(f'**Tramonto** ➡️ {sunset_time}')

    with col2:
        lat = weather_data[7]
        lon = weather_data[8]

        df = pd.DataFrame({
            'lat' : [lat],
            'lon' : [lon]
        })

        st.map(df)


if __name__ == "__main__":
    main()


