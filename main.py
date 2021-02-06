import os
import random
from telegram.ext import Updater
from telegram.ext import CommandHandler
from config import TELEGRAM_TOKEN

import handlers

IMAGES_PATH = './images/'

def get_random_image_path():
    img_path = random.choice(os.listdir(IMAGES_PATH))
    return os.path.join(IMAGES_PATH, img_path)

def get_random_wobmat_fact():
    pass

def get_wobmat_quiz():
    pass

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', handlers.start_handler))
    updater.dispatcher.add_handler(CommandHandler('next', handlers.next_handler))

    updater.start_polling()

if __name__ == '__main__':
    main()