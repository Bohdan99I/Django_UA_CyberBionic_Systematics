from django.http import HttpResponse
from django.shortcuts import render
import requests

def home(request):
    return HttpResponse("<h1>Welcome to Home View</h1>")

def book(request, title):
    return HttpResponse(f"<h2>Book chapter title: {title}</h2>")

def index(request):
    return HttpResponse("<h1>This is Index View</h1>")

def bio(request, username):
    return HttpResponse(f"<h2>Bio of user: {username}</h2>")

def weather(request):
    city = request.GET.get('city')
    if not city:
        return HttpResponse('<script>alert("Please provide a city!");</script>')

    key = "YOUR_APPID"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

    response = requests.get(url)
    data = response.json()

    if data.get('cod') != 200:
        return HttpResponse(f'<script>alert("City {city} does not exist!");</script>')

    country = data['sys']['country']
    name = data['name']
    lon = data['coord']['lon']
    lat = data['coord']['lat']
    weather_main = data['weather'][0]['main']
    temp_kelvin = data['main']['temp']
    temp_celsius = round(temp_kelvin - 273.15, 2)

    context = {
        'country': country,
        'city': name,
        'coords': f"({lon}, {lat})",
        'weather': weather_main,
        'temp': f"{temp_celsius} °C",
    }

    return render(request, 'weather.html', context)
