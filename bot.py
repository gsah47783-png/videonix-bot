import os
import telebot
from openai import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
client = OpenAI(api_key=OPENAI_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🎥 Welcome to Videonix AI!\n\n"
        "Koi bhi video idea ya object bhejo,\n"
        "main usse AI video concept bana dunga 🚀"
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = f"""
You are Videonix AI.
Create a short-form video idea in Hinglish.

Topic: {message.text}

Give:
1. Hook line
2. 15–30 sec script
3. Hashtags
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    bot.reply_to(message, response.choices[0].message.content)

bot.polling()
