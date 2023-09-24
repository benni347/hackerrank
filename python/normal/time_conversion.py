"""
This program converts a time from 12-hour AM/PM format to military (24-hour) time.

:URL: https://www.hackerrank.com/challenges/one-month-preparation-kit-time-conversion/problem
Input: 07:05:45PM
Output: 19:05:45
"""

def timeConversion(s):
    if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:-2]
    elif s[-2:] == "AM":
        return s[:-2]
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    else:
        return str(int(s[:2]) + 12) + s[2:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
