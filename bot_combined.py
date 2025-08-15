import threading
from flask import Flask
from telegram.ext import Updater, CommandHandler

TOKEN = "7978191312:AAFyWVkBruuR42HTuTd_sQxFaKHBrre0VWw"
ADMIN_ID = 7459795138

# Flask web server
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

# Telegram bot
def start(update, context):
    update.message.reply_text("👋 नमस्ते! बॉट चालू है।")

def run_telegram():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    run_telegram()