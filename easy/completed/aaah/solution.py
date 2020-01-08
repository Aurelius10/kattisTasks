import sys
# TASK_URL: https://open.kattis.com/problems/aaah

#sys.stdin = open('test.in')
line1, line2 = sys.stdin.readlines()
if len(line1) > len(line2):
    print("go")
else:
    print("no")
