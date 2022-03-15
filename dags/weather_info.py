import requests
import pandas as pd


#task 1
def curr_weather_data():
    url = 'https://community-open-weather-map.p.rapidapi.com/weather'
    headers = {
        'x-rapidapi-host': 'community-open-weather-map.p.rapidapi.com',
        'x-rapidapi-key': '2ea8674075msh1d4853b18d14611p1af953jsn07b6e4644686'
    }
    cities = ['Jhansi', 'Agra', 'Kanpur', 'Mumbai', 'Pune', 'Amritsar', 'Kolkata', 'Chandigarh', 'Nagpur', 'Patna']
    details = []
    for city in cities:
        querystring = {'q': f'{city},India', 'lat': '0', 'lon': '0', 'id': '2172797',
                       'lang': 'null', 'units': 'imperial', 'mode': 'JSON'}
        response = requests.request('GET', url, headers=headers, params=querystring)
        data = response.json()
        info = data['name'], data['weather'][0]['description'], data['main']['temp'], data['main']['feels_like'], \
               data['main']['temp_min'], data['main']['temp_max'], data['main']['humidity'], data['clouds']['all']
        details.append(info)
    df = pd.DataFrame(details, columns=['State', 'Description', 'Temperature', 'Feels_Like_Temperature', 'Min_Temperature',
                                            'Max_Temperature', 'Humidity', 'Clouds'])
    print(df.head())
    df.to_csv('weather.csv', index=False)



# curr_weather_data()


