from django.shortcuts import render
import requests

# Create your views here.

def tempApp(request):
    # city = "gachibowli"
    try:
        city = request.GET.get("city")
        apiKey = '9e9dc8d1d23fbbc35f36643681296e94'
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"
        response = requests.get(url,timeout = 6000) 
        if response.status_code >=500:
            tempApp(request)
        elif response.status_code == 200:
            resp = response.json()
            payload = {
                "city" : resp['name'],
                "weather" : resp['weather'][0]['main'],
                "kelvin": (int(resp['main']['temp'])),# kelvin
                "celcius" : (int(resp['main']['temp'])) - 273,
                "weatherIcon" : resp["weather"][0]['icon']
            }

            context = {"resp":payload}
            return render(request, "index.html", context)
        
    except Exception as ex:
        print(ex)



