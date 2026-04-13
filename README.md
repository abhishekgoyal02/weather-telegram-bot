# Telegram Weather Bot

A Python based Telegram bot that provides real time weather updates and proactive rain alerts using the OpenWeather API.

---

## Features

*  Fetch real time weather data by city
*  Predict rain for the next 12 hours using forecast API
*  Automatic rain alerts (no user input required)
*  Command-based interaction via Telegram Bot API
*  Secure API key management using environment variables
* Cloud Deployment using Render

---

## How It Works

* The bot fetches weather data from the OpenWeather **Current Weather API**
* It uses the **5-day / 3-hour Forecast API** to analyze upcoming weather conditions
* Rain prediction is based on weather condition codes (`< 700`)

---

## Tech Stack

* **Language:** Python 3.x
* **Framework:** python-telegram bot (v20+)
* **HTTP Client:** requests
* **Environment Management:** python-dotenv
* **API Provider:** OpenWeather API
* **Scheduler:** Built-in JobQueue (telegram.ext)

---

## Installation

```bash
git clone https://github.com/your-username/weather-telegram-bot.git
cd weather-telegram-bot
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```
BOT_TOKEN=your_telegram_bot_token
WEATHER_API_KEY=your_openweather_api_key
```

---

## Commands

```
/start
/weather <city>
```

Example:

```
/weather chandigarh
/weather delhi
```

---

## Automatic Alerts

* Users are registered via `/start`
* The bot runs a scheduled task 
* If rain is predicted within the next 12 hours:

  * A notification is sent automatically

---

## API Details

### Current Weather Endpoint

```
https://api.openweathermap.org/data/2.5/weather
```

### Forecast Endpoint

```
https://api.openweathermap.org/data/2.5/forecast
```

### Key Parameters

* `q` → City name
* `appid` → API key
* `units=metric` → Temperature in Celsius
* `cnt=4` → Next 12 hours (4 × 3-hour intervals)

---

## Notes

* `.env` file is excluded using `.gitignore`
* Do not expose API keys in public repositories
* Requires active internet connection
* Free hosting may have cold start delays

---

## Future Improvements

* Multiuser city preference storage (database)
* Live location based weather (GPS)
* Web dashboard (optional)
* Daily weather summaries

---

## License

This project is licensed under the [MIT License](LICENSE).