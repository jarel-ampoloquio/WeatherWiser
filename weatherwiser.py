import requests

API_KEY = "c769208c7643f4e61aeaf6acfd6e748b"

def ascii_weather(desc):
    desc = desc.lower()

    if "clear" in desc or "sun" in desc:
        return "clear:\n" + r"""
     \   /  
      .-.     
   ― (   ) ―  
      `-’     
     /   \    
"""

    if "cloud" in desc:
        return "cloud:\n" + r"""
   .--.  
 .-(    ).  
(___.__)__)  
"""

    if "rain" in desc:
        return "rain:\n" + r"""
     .-.      
    (   ).    
   (___(__)   
    ‘ ‘ ‘ ‘   
    ‘ ‘ ‘ ‘  
"""

    if "storm" in desc or "thunder" in desc:
        return "storm:\n" + r"""
     .-.     
    (   ).   
   (___(__)  
    ⚡⚡⚡⚡⚡  
"""

    if "snow" in desc:
        return "snow:\n" + r"""
     .-.     
    (   ).    
   (___(__)   
    * * * *   
    * * * *   
"""

    return "unknown weather condition"

def travel_tip(temp, cond):
    cond = cond.lower()
    if "rain" in cond:
        return "Bring an umbrella ☔"
    if "snow" in cond:
        return "Wear thermal layers ❄️"
    if temp > 30:
        return "Stay hydrated and avoid direct sunlight 🥤☀️"
    if temp < 15:
        return "Wear a jacket 🧥"
    return "Weather is good for travel 🚗"

def clothing_suggestion(temp):
    if temp > 30: return "Light shirt, shorts 👕🩳"
    if temp > 20: return "T-shirt and jeans 👕👖"
    if temp > 10: return "Jacket recommended 🧥"
    return "Thick jacket & warm clothes 🧥🧣"

def uv_risk(temp):
    if temp < 20: return "Low UV risk 🟢"
    if temp < 30: return "Moderate UV risk 🟡"
    return "High UV risk 🔴 — Wear sunscreen!"

def get_weather():
    while True:
        city = input("\nEnter city: ")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        r = requests.get(url)

        if r.status_code != 200:
            print("\nCity not found. Please try again.\n")
            continue

        d = r.json()

        name = d["name"]
        country = d["sys"]["country"]
        temp = d["main"]["temp"]
        feels = d["main"]["feels_like"]
        humidity = d["main"]["humidity"]
        pressure = d["main"]["pressure"]
        wind = d["wind"]["speed"]
        temp_min = d["main"]["temp_min"]
        temp_max = d["main"]["temp_max"]
        cond = d["weather"][0]["description"]

        print(ascii_weather(cond))

        print("=" * 50)
        print(f"       TRAVEL WEATHER REPORT — {name}, {country}")
        print("=" * 50)

        print(f"Temperature           : {temp}°C")
        print(f"Feels Like            : {feels}°C")
        print(f"Condition             : {cond}")
        print(f"Min / Max Temp        : {temp_min}°C / {temp_max}°C")
        print(f"Humidity              : {humidity}%")
        print(f"Pressure              : {pressure} hPa")
        print(f"Wind Speed            : {wind} m/s")

        print("\n" + "-" * 50)
        print("               TRAVEL SUGGESTIONS")
        print("-" * 50)
        print(f"Clothing Suggestion   : {clothing_suggestion(temp)}")
        print(f"Travel Advice         : {travel_tip(temp, cond)}")
        print(f"UV Risk Level         : {uv_risk(temp)}")
        print("-" * 50)

        again = input("\nWould you like to check another city? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("\nThank you for using the Travel Weather Assistant! 🌍✨\n")
            break

get_weather()