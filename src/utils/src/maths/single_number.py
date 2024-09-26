def csFindTheSingleNumber(nums):
    length = len(nums)
    answer_dict = {}
    for i in range(length):
        if answer_dict[str(nums[i])]:
            print(answer_dict[str(nums[i])])
        else:
            answer_dict[str()]


input = [1, 1, 2, 1]
print(csFindTheSingleNumber(input))
