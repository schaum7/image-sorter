# initial
from exif import Image


def get_date(image: Image):
    if image.has_exif:
        return str(my_image.datetime).split(" ")[0].split(":")


with open('example-images\\Camera\\20190803_083141.jpg', 'rb') as image_file:
    my_image = Image(image_file)

print(get_date(my_image))
