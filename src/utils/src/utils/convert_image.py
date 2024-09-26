from PIL import Image
import os
import sys

# from pathlib import Path


def convert_image(
    path,
    original: str,
    name: str or None,
    new_format: "png" or "webp" or "jpg",
):
    im = Image.open(os.path.join(path, original)).convert("RGB")

    new_file_name = (name if name else original.split(".")[0]) + "." + new_format
    if new_file_name.find("/"):
        new_file_name = new_file_name.split("/")[-1]

    im.save(os.path.join(path, new_file_name), new_format)


def convert_png_to_ico(url, name):
    print(url, name)
    icon = Image.open(url)
    icon.save(name + ".ico")


if __name__ == "__main__":
    DEFAULT_PATH = r"C:\Users\Alex\local_images"
    while True:
        orig = input("enter the original file name: ")
        path = input(
            "Enter the file path (relative to /lambda/python/utilities). leave blank for default: "
        )
        if path and path.find("/") == -1:
            path = DEFAULT_PATH + "/" + path
        new_name = input(
            "Enter a new name for the file (leave blank to keep the same): "
        )
        format_ = input("Enter the format you would like for the image: ")
        convert_image(
            os.path.abspath(path if path else DEFAULT_PATH),
            orig,
            new_name if new_name else None,
            format_,
        )

        print("conversion successful.")
        break
