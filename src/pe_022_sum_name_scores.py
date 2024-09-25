from project_euler.utils.score_word import score_word
from project_euler.utils.read_out_file import read_out_file

names = read_out_file("name_scores")


def get_sum_name_scores():
    sorted_names = sorted(names)
    return sum(
        [(sorted_names.index(name) + 1) * score_word(name) for name in sorted_names]
    )
