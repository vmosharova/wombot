import os

from dotenv import load_dotenv

load_dotenv() #берём переменную из .env, но эта переменная будет только в рамках данного py-процесса

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
IMAGES_PATH = './images/'
FACTS_STORE_TYPE = 'hardcoded'