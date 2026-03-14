import requests
import json

# 你的 API Key
api_key = "4b7a03bb170ddcbe4411091cfab6db21"
city = "Beijing"

# API 请求 URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=zh_cn"

# 发送请求
response = requests.get(url)
data = response.json()

# 打印结果
print("=" * 50)
print(f"🌤️  {data['name']} 天气信息")
print("=" * 50)
print(f"天气状况：{data['weather'][0]['description']}")
print(f"温度：{data['main']['temp']}°C")
print(f"体感温度：{data['main']['feels_like']}°C")
print(f"湿度：{data['main']['humidity']}%")
print(f"气压：{data['main']['pressure']} hPa")
print(f"风速：{data['wind']['speed']} m/s")
print(f"能见度：{data['visibility']} 米")
print("=" * 50)
