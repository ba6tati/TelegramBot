import os
from dotenv import load_dotenv
import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

with open('HELP.txt') as f:
    help_txt = f.read()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    keyboard = [
        [
            InlineKeyboardButton('Instagram', url='https://www.instagram.com/krasimir.zhelezov'),
            InlineKeyboardButton('Github', url='https://github.com/ba6tati')
        ]
    ]
    
    options = InlineKeyboardMarkup(keyboard)
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text='I\'m a bot made by @ba6tati!', reply_markup=options)
    
    
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='pong')
    
async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
    
async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=random.randint(1, 6))
    
async def help_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.send_message(chat_id=update.effective_chat.id, text=help_txt)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.environ.get("BOT_TOKEN")).build()
    
    start_handler = CommandHandler('start', start)
    ping_handler = CommandHandler('ping', ping)
    caps_handler = CommandHandler('caps', caps)
    dice_handler = CommandHandler('dice', dice)
    
    application.add_handler(start_handler)
    application.add_handler(ping_handler)
    application.add_handler(caps_handler)
    application.add_handler(dice_handler)
    
    application.run_polling()