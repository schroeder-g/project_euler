import argparse
import os
import time
import fnmatch
from pathlib import Path
from dotenv import load_dotenv
from utils.clean_non_ascii import clean_non_ascii

load_dotenv()

# // TODO: Add support for .env files
# // TODO: Add file path to top of output
# level = root.replace(startpath, '').count(os.sep)
#         indent = ' ' * 4 * (level)
#         print('{}{}/'.format(indent, os.path.basename(root)))
#         subindent = ' ' * 4 * (level + 1)
# // TODO:


def concatenate_directory(input, output_dir=None):
    """This function will concatenate all files in a directory into a maximum of 20 files, each with a maximum size of 500MB."""
    directory = os.path.expanduser(input)
    output_dir = output_dir or f"~/desktop/concat_{int(time.time())}"
    output_dir = os.path.expanduser(output_dir)

    if not os.path.exists(directory):
        print(
            f"Error: Directory {directory} does not exist. Be sure to use an absolute path."
        )
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ignore_dirs = [".git", "migrations", "dist" ".db-data", "node_modules", ".vscode"]
    ignore_files = [
        "*.jpg,",
        "*.png",
        "*.pem",
        ".key",
        "*.svg",
        "*.txt",
        ".yaml",
        ".env*",
        "*[.-]lock*",
        "*ignore",
        "*.d.ts",
        ".DS_Store",
    ]

    max_file_size = 500 * 1024 * 1024  # 500MB
    max_output_files = 20
    output_file_count = 0
    current_file_size = 0
    current_file = None
    total_parsed_files = 0

    for root, dirs, files in os.walk(directory):
        # Print the directory we're in
        print(f"\n__{root}__\n")
        dirs[:] = [
            d
            for d in dirs
            if not any(fnmatch.fnmatch(d, pattern) for pattern in ignore_dirs)
        ]
        for file in files:
            # Expose the file tree
            print(
                f"{' ' * 4 * (root.replace(directory, '').count(os.sep))}{'-'} {file}"
            )
            if any(fnmatch.fnmatch(file, pattern) for pattern in ignore_files):
                continue

            file_path = os.path.join(root, file)
            if current_file_size >= max_file_size or current_file is None:
                if current_file:
                    current_file.close()
                if output_file_count >= max_output_files:
                    print("Error: Exceeded maximum number of output files.")
                    return
                output_file_count += 1
                current_file_path = os.path.join(
                    output_dir, f"chunked_{output_file_count}.txt"
                )
                current_file = open(current_file_path, "w")
                current_file_size = 0

            with open(file_path, "rb") as f:
                content = clean_non_ascii(f.read().decode("utf-8", errors="ignore"))
                header = f"\n\n{'=' * 20}\nFILE: {os.path.relpath(file_path, start=directory)}\n{'=' * 20}\n"
                current_file.write(header)
                current_file.write(content)
                current_file_size += len(header) + len(content)
                total_parsed_files += 1

                print(
                    f"\n\033[1;32mSuccessfully added {file}.\033[0m Current chunk size: {current_file_size / (1024 * 1024):.2f} MB, Total files processed: {total_parsed_files}"
                )

    if current_file:
        current_file.close()

    print(f"Done! Check out {output_dir} for your files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Concatenate files in a directory",
        add_help="How to use",
        prog="concat_dir.py",
    )
    parser.add_argument(
        "input",
        type=str,
        help="Absolute path of the directory. e.g. /Users/username/Desktop/MyFolder",
    )
    parser.add_argument(
        "-output_dir",
        "-output",
        "--o",
        dest="output_dir",
        type=str,
        required=False,
        help="Absolute path for output files",
    )
    args = parser.parse_args()
    print("output_dir", args.output_dir)
    concatenate_directory(args.input, args.output_dir)
