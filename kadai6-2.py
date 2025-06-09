import requests
import pandas as pd
# ------------------------------------------------------------
# 🌤 使用するオープンデータの概要
# 名称：気象庁オープンデータ（天気予報JSON）
# 概要：気象庁が提供する天気予報や警報などの公開JSONデータ
# データの内容：千葉県（120000）の天気予報（今日・明日・明後日）
# エンドポイント：https://www.jma.go.jp/bosai/forecast/data/forecast/120000.json
# ------------------------------------------------------------
APP_ID = 5a62d329e6d668bd6808edb5d96cfe86f18dca10
API_URL  = "https://www.jma.go.jp/bosai/forecast/data/forecast/120000.json"

# 📡 データ取得
response = requests.get(url)
data = response.json()

# ------------------------------------------------------------
# 🧾 構造確認：
# data[0]["timeSeries"][0]["areas"][0] に天気がある
# weathers = ["晴れ", "くもり", "雨"]（3日分）
# times = ["2024-06-09", "2024-06-10", "2024-06-11"]（例）
# ------------------------------------------------------------

# エリア名と天気情報を取得
area_data = data[0]["timeSeries"][0]["areas"][0]
area_name = area_data["area"]["name"]
weathers = area_data["weathers"]

# 日付を取得（timeSeries内のtimeDefineより）
dates = data[0]["timeSeries"][0]["timeDefines"]

# pandas DataFrame に整形
df = pd.DataFrame({
    "地域": [area_name] * len(dates),
    "日付": dates,
    "天気": weathers
})
# 表示
print("==== 千葉県の天気予報 ====")
print(df)
