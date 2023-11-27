# weather_api
Weather Forecast API
This Flask application provides a backend API for retrieving weather forecast data based on user input location. It utilizes the OpenWeatherMap API to fetch weather information and presents it in a JSON format.

Usage
To retrieve weather data for a specific city, make a GET request to the /weather endpoint with the city name as a parameter. Optionally, you can specify the desired temperature unit (celsius or fahrenheit) using the unit parameter.

Bash
curl -X GET http://localhost:5000/weather?city=London&unit=fahrenheit
Use code with caution. Learn more
Response Format
The API returns a JSON object containing the following information:

JSON
{
  "city": "London",
  "temperature": 59.24,
  "humidity": 72,
  "description": "Overcast clouds",
  "timestamp": "2023-11-28 11:42:20",
  "unit": "fahrenheit"
}
Use code with caution. Learn more
Running the API
To run the API, you will need to replace YOUR_API_KEY with your OpenWeatherMap API key. You can then run the following command:

Bash
python weather_api.py
Use code with caution. Learn more
This will start the Flask application, and it should listen for requests on http://127.0.0.1:5000.
