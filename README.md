# 🌤️ Travel Weather Assistant (Python CLI Tool)

The **Travel Weather Assistant** is a Python-based command-line application that retrieves real-time weather data using the **OpenWeatherMap API** and provides:

- ASCII art weather visualization  
- Travel clothing suggestions  
- UV risk assessment  
- Travel advice based on temperature and conditions  
- Automatic re-run option for multiple cities  

---

## 🚀 Features

### ✔ Real-time weather data  
Fetches temperature, condition, humidity, pressure, wind speed, and min/max temp.

### ✔ ASCII Weather Icons  
Displays a visual representation of the weather (sun, clouds, rain, snow, storm).

### ✔ Smart Travel Tips  
Recommends:
- Clothing based on temperature  
- UV exposure warnings  
- Travel safety tips (rain, snow, heat, etc.)

### ✔ User-Friendly Loop  
Allows checking multiple cities without restarting the script.

---

## 📦 Requirements

Install dependencies:

```
pip install requests
```

You also need an API key from **OpenWeatherMap**:  
https://openweathermap.org/api

Replace this placeholder in the code:

```
API_KEY = "YOUR_API_KEY_HERE"
```

---

## 🛠 How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Run the script:

```
python weather.py
```

3. Enter any city name to view the weather and travel suggestions.

---

## 📜 Example Output

```
        .-.     
       (   ).   
      (___(__)  
       ‘ ‘ ‘ ‘   
       ‘ ‘ ‘ ‘  

==================================================
       TRAVEL WEATHER REPORT — Tokyo, JP
==================================================
Temperature           : 18°C
Feels Like            : 17°C
Condition             : light rain
Min / Max Temp        : 16°C / 20°C
Humidity              : 82%
Pressure              : 1012 hPa
Wind Speed            : 3.2 m/s
--------------------------------------------------
               TRAVEL SUGGESTIONS
--------------------------------------------------
Clothing Suggestion   : T-shirt and jeans 👕👖
Travel Advice         : Bring an umbrella ☔
UV Risk Level         : Moderate UV risk 🟡
--------------------------------------------------
```

---

## 🧱 Project Structure

```
📁 travel-weather-assistant/
 ├── weather.py        # Main script
 ├── README.md         # Documentation
 └── requirements.txt  # Dependencies (optional)
```

---

## 👨‍💻 Built With

- Python 3  
- OpenWeatherMap API  
- ASCII Art  
- Simple conditional logic & functions  

---

## ⚠️ Important Notes

- Do **NOT** commit your real API key to GitHub.  
- Create a `.env` file or store your API key securely.

Example:

```
API_KEY=your_key_here
```

---

## 📬 Contributing

Pull requests are welcome!

---

## 📄 License

MIT License
