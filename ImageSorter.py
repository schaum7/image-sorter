# initial
from exif import Image
from shutil import copyfile
import os
# path_with_exif_images = "example-images/camera"
# path_all_images = "example-images"


def get_date(image: Image):
    if image.has_exif:
        date = str(image.datetime).split(" ")[0].split(":")
        date.pop()
        return date
    else:
        return "noExif"


def get_dates(path: str):
    image_dates = []
    for image in get_images_paths(path):
        with open(image, 'rb') as image_file:
            my_image = Image(image_file)
        image_dates.append(get_date(my_image))
    return image_dates


def get_images_paths(path: str):
    images = []
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path):
            sub_images = get_images_paths(full_path)

            for i in sub_images:
                images.append(i)
        elif file.endswith(".jpg"):
            images.append(os.path.join(path, file))

    return images


def analyze_directory(path: str):
    exif_files = 0
    non_exif_files = 0
    images = get_images_paths(path)
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


def create_destination_directory(destination_path: str, date: str):
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
            raise OSError(
                "Beim Erstellen vom Ordner {0} ging etwas schief".format(path))
        else:
            print("Ordner {0} erstellt".format(path))

    return path


def sort_images(source_path: str, destination_path: str):
    """ Copies and sorts image from source path into destination path. 
    It also creates a directory structure depending on the year and month the image was taken.
    It sorts the images into that structure.

    Arguments:
        source_path {str} -- directory the images are at currently
        destination_path {str} -- directory you want the images to be sorted at
    """

    for image_path in get_images_paths(source_path):
        with open(image_path, 'rb') as image_file:
            my_image = Image(image_file)

        target_path = create_destination_directory(
            destination_path, get_date(my_image))

        copyfile(image_path, os.path.join(
            target_path, image_path.split("\\")[-1]))
