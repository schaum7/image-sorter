# initial
from exif import Image
import os
path_with_exif_images = "example-images/camera"


def get_date(image: Image):
    if image.has_exif:
        return str(image.datetime).split(" ")[0].split(":")


def get_dates(path: str):
    image_dates = []
    for image in get_images("example-images/camera"):
        with open(image, 'rb') as image_file:
            my_image = Image(image_file)
        image_dates.append(get_date(my_image))
    return image_dates


def get_images(path: str):
    images = []
    for image in os.listdir(path):
        if image.endswith(".jpg"):
            images.append(os.path.join(path, image))
    return images


def analyze_directory(path: str):
    exif_files = 0
    non_exif_files = 0
    images = get_images(path)
    files_count = len(images)

    for file in images:
        with open(file, 'rb') as image_file:
            image = Image(image_file)

        if image.has_exif:
            exif_files += 1
        else:
            non_exif_files += 1

    return [files_count, exif_files, non_exif_files]
    # return "total: " + str(files_count) + ", exif: " + str(exif_files) + ", no exif: " + str(non_exif_files)

# kann nicht richtig funktionieren für den Fall "2018, August; 2019, August"
# def get_years_and_months(path: str):
#     years_and_months = {"years": [], "months": []}
#     for date in get_dates(path):
#         if not date[0] in years_and_months["years"]:
#             years_and_months["years"].append(date[0])
#         if not date[1] in years_and_months["months"]:
#             years_and_months["months"].append(date[1])
#     return years_and_months


# print(get_years_and_months(path_with_exif_images))

os.mkdir("target-directory")

# for date in get_dates(path_with_exif_images):
