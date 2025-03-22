import requests

city = input("Enter city: ")
api_key = "YOUR_OPENWEATHERMAP_API_KEY"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url).json()
if response["cod"] == 200:
    print(f"🌡 Temperature: {response['main']['temp']}°C")
    print(f"🌤 Weather: {response['weather'][0]['description']}")
else:
    print("❌ City not found!")
