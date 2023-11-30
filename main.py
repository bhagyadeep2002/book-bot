import telegram
from dotenv import load_dotenv
import requests
import logging
import random
from telegram import Update
from telegram import ParseMode
from telegram.ext import MessageHandler, Filters
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import CommandHandler
from commands.books import getBook
import os

load_dotenv()

updater = Updater(token=os.environ["TG_BOT"])
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="bot will be abandoned because of lack of confidence")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(text="Please use /book to request book info")

book_handler = CommandHandler('book', getBook)

dispatcher.add_handler(book_handler)

updater.start_polling()