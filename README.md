# 🌦️ Django Weather App

A simple Django project that lets users check current weather conditions by city using the [WeatherAPI](https://www.weatherapi.com/) service.

## 🔧 Features

- Search weather by city name
- Live temperature, condition, icon, and location
- Responsive modern UI
- Secured API key using `.env`

## 🖥️ Tech Stack

- Python 3
- Django 5.x
- WeatherAPI.com (JSON API)
- HTML/CSS (no JS needed)
- python-dotenv for security

## 🚀 Getting Started

```bash
git clone https://github.com/Pradeeptadi/django-weather-app.git
cd django-weather-app
pip install -r requirements.txt

python manage.py runserver


# Rename this file to .env and insert your key
WEATHER_API_KEY=your_api_key


git add README.md .env.example
git commit -m "Add README and .env.example"
git push
