import os
import random

from telegram.ext import Updater
from telegram.ext import CommandHandler

import images_store
import config

TEXT_START = '''Hi there, I'm a Wombot! You can get your daily wombat by sending these commands: (...)'''

def start_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=TEXT_START)

#отправить рандомного вомбата
def next_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Wombat for every occasion")
    context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=open(images_store.get_random_image_path(), 'rb'))