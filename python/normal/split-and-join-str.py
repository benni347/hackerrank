"""This file will split a string at a space and then join it again with a hyphen."""
#!/usr/bin/env python

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)