import sys
#sys.stdin = open('ABC1.in')
line1, line2 = sys.stdin.readlines()
if len(line1) > len(line2):
    print("go")
else:
    print("no")
