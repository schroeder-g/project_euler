from itertools import groupby


def get_max_avg(scores):
    grouped_scores = []

    def key_func(k):
        return k.ge

    for key, group in groupby(scores, scores.keys()):
        grouped_scores.append(group)

    def mean(group):
        return sum(group) / len(group)

    return max(map(grouped_scores, mean))


test = [{"Alex": 88.0}, {"Alex": 88.0}, {"Alex": 88.0}, {"Jenny": 88.5}, {"Alex": 92.0}]

print(get_max_avg(test))
