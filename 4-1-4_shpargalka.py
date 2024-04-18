from os import getenv

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


API_TOKEN = 'YOUR_API_TOKEN'
bot = telebot.TeleBot(getenv('API_TOKEN') or API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("1"))
    markup.add(KeyboardButton("2"))
    bot.reply_to(message, "Привет, укажи номер билета (1, 2, 3).", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == "1":
        bot.reply_to(message,
                     "Излучение — это энергия, которая перемещается из одного места в другое в таком виде, который можно описать как волны или частицы.")
    elif message.text == "2":
        bot.reply_to(message,
                     "Распространение тепла перемещающимися струями газа или жидкости называется конвекцией.")
    else:
        bot.reply_to(message,"Не понял")


bot.infinity_polling()
