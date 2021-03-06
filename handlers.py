import texts

from scheduling import schedule_wobmat_fact, schedule_wobmat_pic
from facts_store import get_facts_store
from images_store import ImagesStore

facts = get_facts_store()
images = ImagesStore()

def start_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=texts.TEXT_START)

def pic_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=texts.TEXT_NEXTIMAGE)
    context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=open(images.get_random_image_path(), 'rb'))

def fact_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=facts.get_random_wombat_fact())


def schedule_pic_handler():
    return schedule_wobmat_pic()

def schedule_fact_handler():
    return schedule_wobmat_fact()