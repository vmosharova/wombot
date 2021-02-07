import os
import random

import config

def get_random_image_path():
    img_path = random.choice(os.listdir(config.IMAGES_PATH))
    return os.path.join(config.IMAGES_PATH, img_path)