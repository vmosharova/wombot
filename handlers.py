import os
import random
from telegram.ext import Updater
from telegram.ext import CommandHandler
from config import TELEGRAM_TOKEN

IMAGES_PATH = './images/'


def start_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi there, I'm a Wombot! You can get your daily wombat by sending these commands:")

#отправить рандомного вомбата
def next_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Wombat for every occasion")
    context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=open(get_random_image_path(), 'rb'))