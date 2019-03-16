def bracket_count(str):
    num = 0
    for i in str:
        if i == "(":
            num += 1
        elif i == ")":
            num -= 1
        if num < 0:
            return "not match"
    if num != 0:
        return "not match"
    else:
        return "match"


if __name__ == '__main__':
    str = "((((((())))))"
    b = bracket_count(str)
    print(b)