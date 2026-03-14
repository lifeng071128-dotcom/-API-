# 免费开源 API 资源集合

## 📋 目录
- [天气 API](#天气-api)
- [地图 API](#地图-api)
- [AI/大模型 API](#ai大模型-api)
- [其他实用 API](#其他实用-api)

## 天气 API
### 1. OpenWeatherMap
- 官网：https://openweathermap.org/api
- 免费额度：每月60次调用
- 需要注册获取 API Key

### 2. 和风天气
- 官网：https://dev.qweather.com/
- 免费额度：每日1000次调用
- 需要注册获取 API Key

## 地图 API
### 1. 高德地图 API
- 官网：https://lbs.amap.com/
- 免费额度：每日5000次调用

## AI/大模型 API
### 1. OpenAI API
- 官网：https://platform.openai.com/
- 免费额度：新用户有试用额度

## 使用说明
1. 注册对应平台账号
2. 获取 API Key
3. 按照文档调用接口
# -API-
收集免费开源API资源，便于学习和使用
## ✅ 已测试 API

### OpenWeatherMap 天气 API
- **测试时间**：2024年X月X日
- **测试结果**：✅ 成功
- **API Key**：已创建（第一个默认密钥）
- **免费额度**：每月 60,000 次调用
- **测试城市**：北京

#### 返回数据示例
```json
{
  "name": "Beijing",
  "main": {"temp": 9.94, "humidity": 27},
  "weather": [{"description": "阴，多云"}],
  "cod": 200
}
