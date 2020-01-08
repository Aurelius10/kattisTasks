import sys
# TASK_URL: https://open.kattis.com/problems/autori

#sys.stdin = open('test.in')
string = sys.stdin.readlines()[0]
res = ''
big = True
for char in string:
    if big:
        res = res + char
        big = False
    if char == "-":
        big = True
print(res)
