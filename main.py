import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()
from weather import get_weather, will_rain_next_12_hours
from alerts import send_rain_alert, users

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    users.add(chat_id)

    await update.message.reply_text(
        "You will now receive automatic rain alerts!\nUse /weather <city>"
    )


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Example: /weather delhi")
        return

    city = " ".join(context.args)

    temp, condition = get_weather(city)
    rain = will_rain_next_12_hours(city)

    if temp is None:
        await update.message.reply_text("City not found")
        return

    msg = f"City: {city.title()}\nTemprature: {temp}°C\nWeather: {condition}"

    if rain:
        msg += "\n🌧Rain expected in next 12 hours!"
    else:
        msg += "\n☀No rain expected"

    await update.message.reply_text(msg)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("weather", weather))
app.job_queue.run_repeating(send_rain_alert, interval=3600, first=10)

print("Bot running...")
app.run_polling()
