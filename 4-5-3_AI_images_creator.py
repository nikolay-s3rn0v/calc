from io import BytesIO

import requests
import telebot

API_TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(API_TOKEN)

HUGGING_FACE_TOKEN = "YOUR_HUGGING_FACE_TOKEN"

HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"


def generate_image(prompt):
    b = requests.post(
        HUGGING_FACE_API_URL,
        headers={"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"},
        json={"inputs": prompt},
    )
    image_content = BytesIO(b.content)
    return image_content


@bot.message_handler(func=lambda message: True)
def handle_private_message(message):
    prompt = message.text.strip()

    image_content = generate_image(prompt)

    bot.send_photo(message.chat.id, image_content)


bot.polling()
