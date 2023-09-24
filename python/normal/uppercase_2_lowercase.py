#!/usr/bin/env python


def swap_case(s):
    s = list(s)
    x = []
    for i in s[:]:
        i = "".join(map(str, i))

        i = str(i)
        lo = i
        if lo.islower():
            upe = i.upper()
            x += [upe]
        elif lo.isupper():
            lowe = i.lower()
            x += [lowe]
        else:
            x += [lo]
    x = "".join(map(str, x))

    return x


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
