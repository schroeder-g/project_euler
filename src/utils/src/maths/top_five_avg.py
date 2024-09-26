def csAverageOfTopFive(scores):
    scores_by_student = {}
    return_avgs = []
    for score in scores:
        if score[0] in scores_by_student:
            scores_by_student[score[0]].append(score[1])
        else:
            scores_by_student[score[0]] = [score[1]]
    for key in scores_by_student:
        the_sum = sum(sorted(scores_by_student[key])[-6:-1:1])
        print(key, ":", reversed(sorted(scores_by_student[key])), the_sum)
    return return_avgs


print(csAverageOfTopFive([[1, 2], [2, 62], [2, 61], [2, 63], [2, 64], [2, 65]]))
