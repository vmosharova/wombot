import unittest
from unittest import mock
from io import BytesIO
from PIL import Image

from images_store import ImagesStore

class ImagesStoreTestCase(unittest.TestCase):

    def create_temporary_image(self):
        in_memory_file = BytesIO()
        image = Image.new('RGBA',
                          size=(0, 0),
                          color=(155, 0, 0))
        image.save(in_memory_file,
                   'png')
        in_memory_file.name = 'tmp_testing_name.png'
        in_memory_file.seek(0)
        # Или: file_mock = mock.Mock(spec=File, name='FileMock')
        #      file_mock.name = 'test.png' ?
        return in_memory_file
        #Или: return file_mock


    def test_get_random_image_path(self):
        with mock.patch('images_store.get_random_image_path', 'create_temporary_image'):
            #как проверить? Надо сделать так, чтобы get_random_image_path возвращал path, а не image


def get_random_image_path(self):
    img_path = random.choice(os.listdir(config.IMAGES_PATH))
    return os.path.join(config.IMAGES_PATH, img_path)

if __name__ == "__main__":
    unittest.main()

