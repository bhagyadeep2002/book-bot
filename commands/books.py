import telegram
from dotenv import load_dotenv
import os
import requests
from telegram import Update
from telegram import ParseMode
from telegram.ext import MessageHandler, Filters
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import CommandHandler
import os

def getBook(update: Update, context: CallbackContext):
    book = context.args
    book_name = "+".join(book)
    api_string = f'https://www.googleapis.com/books/v1/volumes?q={book_name}'
    r = requests.get(api_string)
    data = r.json()
    exact_match = data['items'][0]
    book = f"<b> Title: </b>{exact_match['volumeInfo']['title']} \n"
    book += f"✍️: {exact_match['volumeInfo']['authors'][0]}\n"
    book += f"📖 : {exact_match['volumeInfo']['pageCount']}\n"
    book += f"<b> Description </b>: {exact_match['volumeInfo']['description']} \n"
    book += f"<a href='{exact_match['volumeInfo']['imageLinks']['thumbnail']}'>&#8205;</a>"
    update.message.reply_text(text=book,parse_mode=ParseMode.HTML)
    