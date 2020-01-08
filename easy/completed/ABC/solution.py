import sys
# TASK_URL: https://open.kattis.com/problems/abc

#sys.stdin = open('test.in')
lines = sys.stdin.readlines()
numbers = lines[0].split()
numbers = [int(i) for i in numbers]
numbers.sort()
el = []
for char in lines[1]:
    if char == "A":
        el.append(0)
    elif char == "B":
        el.append(1)
    else:
        el.append(2)
print(numbers[el[0]], numbers[el[1]], numbers[el[2]])
