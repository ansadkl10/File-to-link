from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from flask import Flask, send_from_directory
import os

TOKEN = "8314442394:AAFNA9pb5de-e-2KB6n_qjmlCk3aKzttwEI"

app_web = Flask(__name__)

# create folder
if not os.path.exists("downloads"):
    os.makedirs("downloads")

@app_web.route('/files/<filename>')
def get_file(filename):
    return send_from_directory('downloads', filename)

async def file_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document
    
    if file:
        file_name = file.file_name
        new_file = await context.bot.get_file(file.file_id)
        
        file_path = f"downloads/{file_name}"
        await new_file.download_to_drive(file_path)
        
        link = f"https://YOUR_APP_NAME.onrender.com/files/{file_name}"
        
        await update.message.reply_text(
            f"✅ Link Generated!\n\n"
            f"{link}"
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.Document.ALL, file_handler))

# run both
import threading

def run_bot():
    app.run_polling()

def run_web():
    app_web.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_bot).start()
run_web()
