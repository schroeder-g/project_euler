import os
import ast


def read_out_file(path, lines: bool = False):
    file_path = os.path.expanduser(
        f"~/scripts/py/src/project_euler/out/{path}.txt"
    )

    if lines:
        with open(file_path) as file:
            content = file.readlines()
        return [line.rstrip() for line in content]

    with open(file_path, "r") as file:
        content = file.read()

    file.close()

    return ast.literal_eval(content)
    # return ['932718654']
