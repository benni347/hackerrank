"""mutate the string at a given position with a given char."""
#!/usr/bin/env python

def mutate_string(string, position, character):
    s = string
    p1 = position
    c = character
    p2 = p1 + 1
    ns = s[:p1] + c + s[p2:]
    # print(ns)
    return ns

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)