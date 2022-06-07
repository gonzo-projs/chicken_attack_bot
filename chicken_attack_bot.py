import os
from dotenv import load_dotenv
import telebot
import json
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
print()
print("The Key: " + str(API_KEY))

bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "It's Chicken AttaaaaAAAaaack")

@bot.message_handler(commands=['c'])
def send_image_uri(message):

    print(message.text)
    name = message.text[5:]
    params = {"fuzzy":name}
    json = requests.get(url="https://api.scryfall.com/cards/named", params=params)
    json=json.json()
    image = json['image_uris']['normal']
    
    bot.reply_to(message, image)
    # bot.reply_to(message, message.text)

bot.infinity_polling()