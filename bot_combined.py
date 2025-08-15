import telebot
from keep_alive import keep_alive

BOT_TOKEN = "8418715308:AAFApWpbwdBzpaemol41ptWzudI-YdM2tIg"
ADMIN_ID = 7459795138

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 नमस्ते! आपका Telegram बॉट Render पर चल रहा है ✅")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"आपने कहा: {message.text}")

keep_alive()

bot.polling(non_stop=True)