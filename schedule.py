import schedule

import config
import facts_store
import images_store

def schedule_wobmat_pic:
    pass
    #schedule.every().day.at("08:00").do(images_store.get_random_image_path())

def schedule_wobmat_fact:
    pass
    #schedule.every().day.at("08:00").do(fact_store.get_random_wobmat_fact())