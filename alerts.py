from weather import will_rain_next_12_hours
users = set()
CITY = "chandigarh"
async def send_rain_alert(context):
    rain = will_rain_next_12_hours(CITY)

    if rain:
        for user in users:
            await context.bot.send_message(
                chat_id=user,
                text=f"🌧Rain alert!\nRain expected in next 12 hours in {CITY.title()} ☂"
            )