import os
import random

import config


class ImagesStore:

    def get_random_image_path(self):
        img_path = random.choice(os.listdir(config.IMAGES_PATH))
        return os.path.join(config.IMAGES_PATH, img_path)
