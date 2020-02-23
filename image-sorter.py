# initial
from exif import Image
import os


def get_date(image: Image):
    if image.has_exif:
        return str(image.datetime).split(" ")[0].split(":")


def get_images(path: str):
    images = []
    for image in os.listdir(path):
        if image.endswith(".jpg"):
            images.append(os.path.join(path, image))
    return images


images = get_images("example-images\\Camera")
for image in images:
    with open(image, 'rb') as image_file:
        my_image = Image(image_file)
    print(get_date(my_image))


# print(get_date(my_image))
