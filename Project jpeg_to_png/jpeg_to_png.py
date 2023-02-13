from PIL import Image
import os
import sys

images_folder = sys.argv[1]
save_converted_images = sys.argv[2]

if not os.path.exists(save_converted_images):
   os.mkdir(save_converted_images)

list_images_folder = os.listdir(images_folder)

for images in list_images_folder:
   img = Image.open(rf'{images_folder}{images}')
   clean_name = os.path.splitext(images)[0]
   img.save(rf'{save_converted_images}{clean_name}.png','png')
   print('Done')



