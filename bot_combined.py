import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔑 Config
BOT_TOKEN = "7978191312:AAFyWVkBruuR42HTuTd_sQxFaKHBrre0VWw"
ADMIN_ID = 7459795138
REQUIRED_CHANNEL = "boomupbot10"   # आपका group/channel username (बिना @ के)
WEBAPP_URL = "https://studiokbyt.onrender.com"

# लॉगिंग
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat_id = update.effective_chat.id

    try:
        member = await context.bot.get_chat_member("@" + REQUIRED_CHANNEL, user.id)

        if member.status in ["member", "administrator", "creator"]:
            # ✅ User already joined
            keyboard = [[InlineKeyboardButton("🌐 WebApp खोलें", web_app=WebAppInfo(url=WEBAPP_URL))]]
            await update.message.reply_text(
                "✅ आपने Join कर लिया है!\nअब WebApp खोलें 👇",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            # ❌ Not joined
            keyboard = [[InlineKeyboardButton("✅ मैंने Join कर लिया", callback_data="check_join")]]
            await update.message.reply_text(
                f"🚨 पहले हमारे ग्रुप को Join करें:\n👉 https://t.me/{REQUIRED_CHANNEL}",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

    except Exception as e:
        keyboard = [[InlineKeyboardButton("✅ मैंने Join कर लिया", callback_data="check_join")]]
        await update.message.reply_text(
            f"⚠️ पहले हमारे ग्रुप को Join करें:\n👉 https://t.me/{REQUIRED_CHANNEL}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

# Callback: ✅ मैंने Join कर लिया
async def check_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user

    member = await context.bot.get_chat_member("@" + REQUIRED_CHANNEL, user.id)

    if member.status in ["member", "administrator", "creator"]:
        keyboard = [[InlineKeyboardButton("🌐 WebApp खोलें", web_app=WebAppInfo(url=WEBAPP_URL))]]
        await query.message.reply_text(
            "✅ Verification Successful!\nअब WebApp खोलें 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await query.message.reply_text(
            f"❌ आपने अभी तक Join नहीं किया!\n👉 पहले यहाँ Join करें: https://t.me/{REQUIRED_CHANNEL}"
        )

    await query.answer()

# सिर्फ Admin के लिए command
async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        await update.message.reply_text("👑 Admin Panel में आपका स्वागत है!")
    else:
        await update.message.reply_text("❌ केवल Admin इस command का उपयोग कर सकते हैं।")

# 🚀 Run Bot
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin))
    app.add_handler(CallbackQueryHandler(check_join, pattern="check_join"))

    print("🤖 Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()