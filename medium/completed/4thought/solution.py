import sys
# TASK_URL: https://open.kattis.com/problems/4thought

#sys.stdin = open('problemA.in')
lines = sys.stdin.readlines()
num_lines = int(lines[0])
ones = 4
ones_string = "4"
twos = [1, 16]
twos_string = ["4 / 4", "4 * 4"]
threes = [0, 4, 64]
threes_string = ["4 / 4 / 4", "4 * 4 / 4", "4 * 4 * 4"]
fours = [0, 1, 16, 256]
fours_string = ["4 / 4 / 4 / 4", "4 * 4 / 4 / 4", "4 * 4 * 4 / 4", "4 * 4 * 4 * 4"]
op = [" + ", " - "]
def one_one_two(num, op=op, ones=ones, ones_string=ones_string, twos=twos, twos_string=twos_string):
    for operator1 in op:
        if operator1 == " + ":
            res_temp = ones + ones
        else:
            res_temp = ones - ones
        for operator2 in op:
            for j in range(2):
                if operator2 == " + ":
                    res = res_temp + twos[j]
                else:
                    res = res_temp - twos[j]
                if res == num:
                    return ones_string + operator1 + ones_string + operator2 + twos_string[j] + " = " + str(num)
    return "0"

def two_one_one(num, op=op, twos=twos, twos_string=twos_string, ones=ones, ones_string=ones_string):
    for j in range(2):
        res = twos[j] - ones - ones
        if res == num:
            return twos_string[j] + op[1] + ones_string + op[1] + ones_string + " = " + str(num)
    return "0"            

def one_three(num, op=op, ones=ones, ones_string=ones_string, threes=threes, threes_string=threes_string):
    for operator1 in op:
        for j in range(3):
            if operator1 == " + ":
                res = ones + threes[j]
            else:
                res = ones - threes[j]
            if res == num:
                return ones_string + operator1 + threes_string[j] + " = " + str(num)
    return "0"

def three_one(num, op=op, threes=threes, threes_string=threes_string, ones=ones, ones_string=ones_string):
    for j in range(3):
        res = threes[j] - ones
        if res == num:
            return threes_string[j] + op[1] + ones_string + " = " + str(num)
    return "0"

def two_two(num, op=op, twos=twos, twos_string=twos_string):
    for operator1 in op:
        for j in range(2):
            for k in range(2):
                if operator1 == " + ":
                    res = twos[j] + twos[k]
                else:
                    res = twos[j] - twos[k]
                if res == num:
                    return twos_string[j] + operator1 + twos_string[k] + " = " + str(num)
    return "0"

def four(num, fours=fours, fours_string=fours_string):
    for j in range(4):
        if fours[j] == num:
            return fours_string[j] + " = " + str(num)
    return "0"

for i in range(1, num_lines+1):
    num = int(lines[i])
    if num > 68:
        if num == 256:
            print("4 * 4 * 4 * 4 = 256")
        else:
            print("no solution")
        continue
    if num < -60:
        print("no solution")
        continue
    res = one_one_two(num=num)
    if res != "0":
        print(res)
        continue
    res = two_one_one(num=num)
    if res != "0":
        print(res)
        continue
    res = one_three(num=num)
    if res != "0":
        print(res)
        continue
    res = three_one(num=num)
    if res != "0":
        print(res)
        continue
    res = two_two(num=num)
    if res != "0":
        print(res)
        continue
    res = four(num=num)
    if res != "0":
        print(res)
        continue
    print("no solution")    
    
        
