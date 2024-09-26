import os


def cat_file(path, file_name):
    lines = []
    # Generate the full path for the given file
    file_path = os.path.join(path, file_name)
    # Read the file
    with open(file_path) as file:
        for line in file:
            # rstrip to remove trailing "\n"
            lines.append(line.rstrip())
        file.close()

    return lines
