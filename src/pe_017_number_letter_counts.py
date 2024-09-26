num_word_map = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety",
    "00": "hundred",
    "000": "thousand",
}


def get_range_num_words():
    spelled = []
    for num in range(1, 1001):
        word = get_num_word(num)
        spelled.append(word)
    return spelled


def get_num_word(num):
    if num < 21:
        return num_word_map[str(num)]
    else:
        n = str(num)
        word = ""
        for i, dig in enumerate(n):
            # Skip zeroes
            if dig == "0":
                continue
            # ones place
            if i == len(n) - 1:
                word += num_word_map[dig]
            # tens place
            elif i == len(n) - 2:
                # handle teens
                if dig == "1":
                    word += num_word_map[n[i:]]
                    break
                # 20 - 99
                else:
                    word += num_word_map[n[i] + "0"]
                    if n[-1] == "0":
                        break
                    word += "-"
            # handle hundreds
            elif i == len(n) - 3:
                word += num_word_map[dig] + " " + num_word_map["00"]
                if n[-1] == "0" and n[-2] == "0":
                    break
                word += " and "
            else:
                word += num_word_map[n[0]] + " " + num_word_map["000"]
        return word


def sum_letter_counts():
    spelled_str = "".join(
        list(filter(lambda list_: list_ != " " and list_ != "-", "".join(get_range_num_words())))
    )
    return len(spelled_str)
