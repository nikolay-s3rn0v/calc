import telebot

API_TOKEN = '...'
bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, как тебя зовут?")


# Handle all other messages with content_type 'text'
# (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"Рад знакомству, {message.text}!")


bot.infinity_polling()
