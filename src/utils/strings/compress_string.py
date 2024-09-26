def compress_string(s):
    ans = ""
    temp = {}

    for i, val in enumerate(s):
        if temp.get(val, 0) == 0:
            temp[val] = 1
            if len(temp) > 1:
                ans += s[i - 1] + str(temp.pop(s[i - 1]))
        else:
            temp[val] += 1
        if i == len(s) - 1:
            ans += s[i] + str(temp[s[i]])

    return ans if len(ans) < len(s) else s


if __name__ == "__main__":
    s = input("Enter string to compress: ")
    print(compress_string(s))
