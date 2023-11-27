import requests
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Set OpenWeatherMap API key
api_key = "9e778dd2398993fe8bba470783778dc6"

@app.route("/weather", methods=["GET"])
def get_weather_data():
    # Retrieve city name and unit preference from request
    city = request.args.get("city")
    unit = request.args.get("unit", "Fahrenheit")

    # Construct API request URL
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # Send API request and extract weather data
    response = requests.get(api_url)
    weather_data = response.json()

    # Process and format weather data
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]

    # Convert temperature to Celsius or Fahrenheit
    if unit.lower() == "Fahrenheit":
        temperature = (temperature - 273.15) * 9/5 + 32

    # Prepare JSON response with additional information
    response_data = {
        "city": city,
        "temperature": temperature,
        "humidity": humidity,
        "description": description,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "unit": unit
    }

    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)
