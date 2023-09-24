def count_substring(string, sub_string):
    s = string
    sub_s = sub_string
    i = 0
    for i in range(0, len(s)):
        if s in sub_s:
            i += 1
        else:
            continue
    return i


if __name__ == "__main__":
    print("input string: ")
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
