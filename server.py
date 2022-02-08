from flask import Flask, request
import requests
import json

app = Flask(__name__)
def havaDurumu(self):
    city = self
    apiKey = 'fb9355977692afdd45177788cfc6f271'
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}')
    weatherData = response.json()

    temp = round((weatherData['main']['temp'] - 273.15), 2)


    havadurumuDict = {

        "temperature": temp,
        
    }

    return havadurumuDict
@app.route("/", methods=['GET'])
def home():
        
        name = {
        "firstname": "AHMET",
        "lastname": "SEKER"     }
            
        return json.dumps(name)


@app.route("/temperature", methods=['GET'])
def weather():


        city = request.args.get("city")
        if not city:
            return '{"message": "Internal Server Error"}'
        else:
            a = havaDurumu(city)
            return json.dumps(a) 



if __name__ == "__main__":

    app.run(debug=True)
