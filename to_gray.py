from PIL import Image
import os

orig_filepath = 'orig'
gray_filepath = 'gray'

for file in os.listdir(orig_filepath):
    image_file = Image.open(os.path.join(orig_filepath, file))
    image_file = image_file.convert('L')
    image_file.save(os.path.join(gray_filepath, file[:-4] + '_gray.png'))