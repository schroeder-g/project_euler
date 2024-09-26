"""This module enables styling terminal output. To use it, import TermStyler like so:
from utilities.terminalprint import TermStyler as ts"""

import os

os.system("color")  # Necessary for Windows


class TermStyler:
    """
    Append styles to your terminal output.
    """

    colors = {
        "mint": [0, 166, 118],
        "pearl": [247, 249, 249],
        "bronze": [106, 179, 96],
        "spearmint": [124, 208, 184],
        "gold": [233, 217, 133],
        "sapphire": [25, 100, 126],
        "plum": [143, 57, 133],
        "mauve": [228, 193, 249],
        "carnation": [255, 153, 200],
        "pleasant_alert": [214, 50, 48],
        "platinum": [234, 234, 234],
    }

    @staticmethod
    def inverse(txt):
        return f"\033[7m{txt}\033[0m"

    @staticmethod
    def bold(txt):
        return f"\033[1m{txt}\033[0m"

    @staticmethod
    def underline(txt):
        return f"\033[4m{txt}\033[0m"

    @staticmethod
    def blink(txt):
        return f"\033[5m{txt}\033[0m"

    @staticmethod
    def colorize(r, g, b, txt):
        return f"\033[38;2;{r};{g};{b}m{txt}\033[0m"

    @staticmethod
    def get_color(c):
        return TermStyler.colors[c]

    @staticmethod
    def get_uni(u):
        return TermStyler.unicode_chars[u]


ts = TermStyler()
