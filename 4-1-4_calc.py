from os import getenv

import telebot


API_TOKEN = 'YOUR_API_TOKEN'
bot = telebot.TeleBot(getenv('API_TOKEN') or API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Привет, я калькулятор. Введите первое число, операцию(+,-,*,/) и второе число через пробел"
    )


@bot.message_handler(func=lambda message: True)
def handle_calculation(message):
    a, operation, b = message.text.split()

    a = float(a)
    b = float(b)

    result = 0
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if a == 0:
            bot.reply_to(message, "На 0 делить нельзя")
            return

        result = a / b
    else:
        bot.reply_to(message, "Неизвестная операция")

    bot.reply_to(message, f"Результат: {result}")


bot.infinity_polling()
