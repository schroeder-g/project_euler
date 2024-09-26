from PIL import Image
import argparse


def fill_transparency(input_file, output_file, fill_color=(255, 255, 255)):
    try:
        with Image.open(input_file) as img:
            if img.mode in ("RGBA", "LA") or (
                img.mode == "P" and "transparency" in img.info
            ):
                alpha = img.convert("RGBA").split()[3]
                bg = Image.new("RGBA", img.size, fill_color + (255,))
                bg.paste(img, mask=alpha)
                bg.convert(img.mode).save(output_file)
                print(f"Image saved as {output_file}")
            else:
                print("Image is not transparent.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fill image transparency.")
    parser.add_argument("-f", "--file", required=True, help="Input file path.")
    parser.add_argument("-o", "--output", required=True, help="Output file path.")
    parser.add_argument(
        "-c", "--color", help="Color to fill transparency with in format <r>,<g>,<b>."
    )
    args = parser.parse_args()

    fill_color = (
        tuple(map(int, args.color.split(","))) if args.color else (255, 255, 255)
    )

    fill_transparency(args.file, args.output, fill_color)
