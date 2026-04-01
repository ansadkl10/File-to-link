from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = "8314442394:AAFNA9pb5de-e-2KB6n_qjmlCk3aKzttwEI"

# create folder
if not os.path.exists("downloads"):
    os.makedirs("downloads")

async def file_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document
    
    if file:
        file_name = file.file_name
        new_file = await context.bot.get_file(file.file_id)
        
        file_path = f"downloads/{file_name}"
        await new_file.download_to_drive(file_path)
        
        await update.message.reply_text(
            f"✅ File saved!\n\n"
            f"Name: {file_name}"
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.Document.ALL, file_handler))

app.run_polling()
# run both
import threading

def run_bot():
    app.run_polling()

def run_web():
    app_web.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_bot).start()
run_web()
