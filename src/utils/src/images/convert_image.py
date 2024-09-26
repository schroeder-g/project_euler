import argparse
from PIL import Image
import os


def convert_image(input_file, output_spec, dimensions=None):
    try:
        # Split output_spec into path and format
        output_path, output_format = os.path.splitext(output_spec)
        if not output_path:  # If output_path is empty, use input file's path
            output_path, _ = os.path.splitext(input_file)
        if not output_format:  # If output_format is empty, exit
            raise ValueError("Output format not specified.")
        output_format = output_format.lstrip(".")

        with Image.open(input_file) as img:
            if dimensions:
                width, height = map(int, dimensions.split("x"))
                img = img.resize((width, height))

            output_file = f"{output_path}.{output_format}"
            img.save(output_file)
            print(f"Image saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert image formats.")
    parser.add_argument("-f", "--file", required=True, help="Input file path.")
    parser.add_argument(
        "-r", "--output-spec", required=True, help="Output path and/or format."
    )
    parser.add_argument(
        "-d", "--dimensions", help="Desired dimensions in format <width>x<height>."
    )
    args = parser.parse_args()
    convert_image(args.file, args.output_spec, args.dimensions)
