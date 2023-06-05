#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Authour:  benni347@github.com

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{0:.2f}".format(sum(student_marks[query_name])/len(student_marks[query_name])))

# Alternative solution:
# #!/usr/bin/env python3
# # https://www.hackerrank.com/challenges/finding-the-percentage/problem
# # Authour:  benni347@github.com
#
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = sum(scores)/len(scores)
#     query_name = input()
#     print("{0:.2f}".format(student_marks[query_name]))
#
