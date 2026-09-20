import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
TOKEN=os.getenv("BOT_TOKEN")
async def balas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.dice:
        await update.message.reply_text(f"Angka dadu : {update.message.dice.value}")
app=ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, balas))
app.run_polling(drop_pending_updates=True)
