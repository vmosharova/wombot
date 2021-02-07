import os
import random

from telegram.ext import Updater
from telegram.ext import CommandHandler

import images_store
import config
import Texts

def start_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=Texts.TEXT_START)

#отправить рандомного вомбата
def next_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=Texts.TEXT_NEXTIMAGE)
    context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=open(images_store.get_random_image_path(), 'rb'))

#отправить рандомный факт
def fact_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(Texts.WOMBAT_FACT))