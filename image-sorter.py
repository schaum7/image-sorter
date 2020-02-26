# initial
from exif import Image
import os
path_with_exif_images = "example-images/camera"


def get_date(image: Image):
    if image.has_exif:
        date = str(image.datetime).split(" ")[0].split(":")
        date.pop()
        return date
    else:
        return "noExif"


def get_dates(path: str):
    image_dates = []
    for image in get_images(path):
        with open(image, 'rb') as image_file:
            my_image = Image(image_file)
        image_dates.append(get_date(my_image))
    return image_dates


def get_images(path: str):
    images = []
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path):
            sub_images = get_images(full_path)

            for i in sub_images:
                images.append(i)
        elif file.endswith(".jpg"):
            images.append(os.path.join(path, file))

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


def create_destination_directories(source_path: str, destination_path: str):
    for date in get_dates(source_path):
        if date == "noExif":
            path = os.path.join(destination_path, "noExif")
        else:
            year = date[0]
            month = date[1]
            path = os.path.join(destination_path, year, month)
        if not os.path.isdir(path):
            try:
                os.makedirs(path)
            except OSError:
                print("Beim Erstellen vom Ordner %s ging etwas schief", path)
            else:
                print("Ordner %s erstellt", path)


create_destination_directories(
    "example-images", os.path.join(os.getcwd(), "target"))
