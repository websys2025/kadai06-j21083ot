import requests
import json

# ---------------------------------------------------------------------
# このプログラムは 気象庁が提供するオープンデータAPI を利用して、
# 「東京都」の最新の天気予報データを取得して表示します。
# ▶ 参照するオープンデータの名前と概要：
#     - 気象庁 天気予報API   
# ▶ エンドポイント（東京都）：
#     - https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json
# ▶ 機能：
#     - JSON形式で地域ごとの天気情報（予報、気温など）を取得する
#
# ▶ 使い方
#     - レスポンスJSONから天気予報や気温を抽出して使用
# ---------------------------------------------------------------------

# APIエンドポイント（東京都の天気予報）
url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"

# APIにリクエストを送信
response = requests.get(url)

# レスポンスの内容を表示
if response.status_code == 200:
    data = response.json()
    
    # 天気予報部分を抽出（先頭のデータ）
    area_weather = data[0]["timeSeries"][0]["areas"][0]["weathers"]
    time_definitions = data[0]["timeSeries"][0]["timeDefines"]

    print("【東京都の天気予報】")
    for time, weather in zip(time_definitions, area_weather):
        print(f"{time}: {weather}")
else:
    print("データの取得に失敗しました。ステータスコード:", response.status_code)
