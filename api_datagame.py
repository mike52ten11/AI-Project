import google.generativeai as genai
import os

api_key = 'YOUR_API_KEY'
genai.configure(api_key = api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

response = model.generate_content("請利用google地圖，查詢緯度25.017370，經度121.531788附近有哪些美食，並使用與Google Weather，查詢並根據今天天氣溫度、濕度與降雨機率幫我安排一下附近行程，今天是2024/06/13(四)平日，我想去咖啡廳，中等預算，想花一整天，有下雨就室內行程，沒下雨就室外行程")

print(response.text)
print(response)

# 單個純文字
# import json
# import requests
# API_KEY = ''
# url = f'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}'
# headers = {'Content-Type': 'application/json'}
# data = {
#     "contents": [
#         {
#             "parts": [{"text": "緯度25.017370，經度121.531788，根據今天天氣溫度、濕度與降雨機率幫我安排一下附近行程，有下雨就室內行程，沒下雨就室外行程"}]
#         }
#     ]
# }
# response = requests.post(url, headers=headers, json=data)
# print(f"response status_code: {response.status_code}")
# print(json.dumps(response.json(), indent=4, ensure_ascii=False))
