# This algorithm involves two steps:
# 1. Sorts the jobs by their finish-time in non-decreasing order
# 2. for each i from 0 - N, calculate the profit available by including the job and excluding it.


class Job:
    def __init__(self, start=1, finish=2, profit=300):
        self.start = start
        self.finish = finish
        self.profit = profit


# Iterative binary search function which returns the latest job that
# does not conflict with the start time of the job at the target index.
# Returns -1 if all previous jobs conflict.
def binary_search(jobs, target_start_index):
    left = 0
    right = target_start_index - 1

    while left <= right:
        current = (left + right) // 2
        if jobs[current].finish <= jobs[target_start_index].start:
            if jobs[current + 1].finish <= jobs[target_start_index].start:
                # because there is a later non-conflicting job, increment bottom
                left = current + 1
            else:
                # Because there's no later non-conflicting job, return
                return current
        else:
            right = current - 1
    return -1


def schedule_jobs(job_list):
    # sort jobs according to their end time
    job_list = sorted(job_list, key=lambda j: j.finish)

    len_ = len(job_list)

    # initialize a table for holding subproblem solutions,
    # i.e. the Maximum returns available for jobs in temporal order.
    table = [0 for _ in range(len_)]
    # initialize first value to solve rest of set.
    table[0] = job_list[0].profit

    # fill in table values
    for i in range(1, len_):
        curr_job_weight = job_list[i].profit

        # find the most recent job with a non-conflicting end-time
        prev_profit_index = binary_search(job_list, i)

        # As long as there's some previous job that isn't conflicting, add the total value accrued at that point to the current
        if prev_profit_index != -1:
            curr_job_weight += table[prev_profit_index]

        # compare value added ,
        table[i] = max(curr_job_weight, table[i - 1])

    print(table)
    return table[len_ - 1]


test = [Job(), Job(1, 3, 800), Job(2, 3, 600), Job(3, 4, 600)]

print(schedule_jobs(test))
