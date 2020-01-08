import sys

sys.stdin = open("test.in")
for i in sys.stdin:
        num = int(i)
        break
n = 0
while num > 2**n:
        n+=1
n+=1
print(n)