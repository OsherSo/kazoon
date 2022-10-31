import os
from PIL import Image


def jpg_to_png_converter(src_dir, dest_dir, image_size=None):
    """
    Convert images from jpg format to png format.

    Arguments:
        src_dir: Folder path where the images with jpg format are located.
        dest_dir: Output folder where the png images will be passed to.
        image_size: The requested size in pixels, as a 2-tuple: (width, height), Default: None.

    Return:
        None
    """
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)

    images_paths = os.listdir(src_dir)
    for image_path in images_paths:
        image = Image.open(src_dir + '/' + image_path)
        if image_size:
            image.thumbnail(image_size)

        image_name = os.path.splitext(image_path)[0]
        image.save(f"{dest_dir}/{image_name}.png", format="png")
