import requests
import os
from dotenv import load_dotenv
from django.shortcuts import render

load_dotenv()  # Load variables from .env

def index(request):
    weather_data = None
    if request.method == "POST":
        city = request.POST.get('city')
        if city:
            api_key = os.getenv("WEATHER_API_KEY")
            url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {"error": "City not found or API issue."}

    return render(request, 'weather/index.html', {'weather_data': weather_data})
