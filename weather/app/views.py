import requests
from django.shortcuts import render

def base(request):
    api_key = 'ddb1da573cd5a20a9bbba6941bfbfff0'  # your actual API key
    weather = {}

    if request.method == 'POST':
        city = request.POST.get('city')

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather = {'error': 'City not found or API error.'}

    return render(request, 'base.html', {'weather': weather})
