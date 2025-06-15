import requests
import json

# ---------------------------------------------------------------------
# このプログラムは 教育統計調査データを取得します。
# 対象データID：000040277626（教育統計調査 学校基本調査）
# APIのエンドポイント：https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
# 利用機能：getStatsData（統計データ取得）

# ---------------------------------------------------------------------

mport requests
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
