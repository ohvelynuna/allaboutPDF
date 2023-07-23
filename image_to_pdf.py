from PIL import Image
import os

folder_path = input(rf"enter the folder path\n > ")
file_type = input('what are you converting (jpg, png)\n > ')
saving_strip = len(file_type) + 1
for filename in os.listdir(folder_path):
    if filename.lower().endswith(file_type):
        image_1 = Image.open(os.path.join(folder_path, filename))
        im_1 = image_1.convert('RGB')
        im_1.save(os.path.join(folder_path, filename[:-saving_strip] + '.pdf'))
        print(filename + "converted to pdf")