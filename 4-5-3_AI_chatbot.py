from os import getenv
from hugchat import hugchat
from hugchat.login import Login

import telebot

API_TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(getenv('API_TOKEN') or API_TOKEN)

HUGGING_FACE_EMAIL = "YOUR_HUGGING_FACE_EMAIL"
HUGGING_FACE_PASSWORD = "YOUR_HUGGING_FACE_PASSWORD"

cookie_path_dir = "./cookies/"
sign = Login(HUGGING_FACE_EMAIL, HUGGING_FACE_PASSWORD)


@bot.message_handler(func=lambda message: True)
def handle_private_message(message):
    prompt = message.text.strip()

    cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

    response = chatbot.chat(prompt)

    bot.send_message(message.chat.id, str(response))


bot.polling()
