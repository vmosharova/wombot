import scheduling

from handlers import pic_handler,fact_handler

def schedule_wobmat_pic:
    scheduling.every().day.at("08:00").do(pic_handler())

def schedule_wobmat_fact:
    scheduling.every().day.at("08:00").do(fact_handler())