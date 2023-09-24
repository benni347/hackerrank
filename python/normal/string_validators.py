#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/string-validators/problem
# Author:  benni347@github.com

if __name__ == "__main__":
    string_to_validate = input()
    print(any(c.isalnum() for c in string_to_validate))
    print(any(c.isalpha() for c in string_to_validate))
    print(any(c.isdigit() for c in string_to_validate))
    print(any(c.islower() for c in string_to_validate))
    print(any(c.isupper() for c in string_to_validate))

# Alternative solution, better optimized:
#
# if __name__ == "__main__":
#     string_to_validate = input()
#     is_alnum, is_alpha, is_digit, is_lower, is_upper = False, False, False, False, False
#
#     for c in string_to_validate:
#         if not is_alnum and c.isalnum():
#             is_alnum = True
#         if not is_alpha and c.isalpha():
#             is_alpha = True
#         if not is_digit and c.isdigit():
#             is_digit = True
#         if not is_lower and c.islower():
#             is_lower = True
#         if not is_upper and c.isupper():
#             is_upper = True
#
#         # If all variables are True, no need to check further.
#         if is_alnum and is_alpha and is_digit and is_lower and is_upper:
#             break
#
#     print(is_alnum)
#     print(is_alpha)
#     print(is_digit)
#     print(is_lower)
#     print(is_upper)
