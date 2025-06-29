
import telebot
from generate_matrix import generate_matrix_pdf

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Отправь свою дату рождения в формате ДД.ММ.ГГГГ")

@bot.message_handler(func=lambda msg: True)
def handle_date(message):
    try:
        pdf_path = generate_matrix_pdf(message.text)
        with open(pdf_path, 'rb') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")

bot.polling()
