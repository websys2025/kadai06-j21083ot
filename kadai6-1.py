import requests
import json

APP_ID = "aed1b1fc27cc6e970968a017cc49d15c2a73cfa8"

API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsList"

params = {
    "appId": APP_ID,
    "statsCode": "00601010",  # 教育統計調査
    "searchKind": 1,
    "limit": 5,
    "lang": "J"
}

response = requests.get(API_URL, params=params)
data = response.json()

print(json.dumps(data, indent=2, ensure_ascii=False))
