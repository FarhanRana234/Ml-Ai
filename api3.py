import requests

API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "411c6456e6b04dee99908c05d66bb68c"

params = {
    "country": "us",
    "apiKey": API_KEY,
    "pageSize": 1
}

response = requests.get(API_URL, params=params)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")