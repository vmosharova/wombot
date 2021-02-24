import os
import random

from telegram.ext import Updater
from telegram.ext import CommandHandler

import config
import handlers

# def get_wombat_quiz():
#     pass

def main():
    updater = Updater(config.TELEGRAM_TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', handlers.start_handler))
    updater.dispatcher.add_handler(CommandHandler('pic', handlers.next_handler))
    updater.dispatcher.add_handler(CommandHandler('fact', handlers.fact_handler))

    updater.start_polling()

if __name__ == '__main__':
    main()