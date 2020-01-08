import sys
import math

get_bin = lambda x, n: format(x, 'b').zfill(n)

def add(x):
    return int((x+1)*x/2)

def zeroOne(tekst):
    counter=0
    summer=0
    for i in range(len(tekst)):
        if tekst[i]=="0":
            counter+=1
            summer+=i+1
    return summer - add(counter)

def input(string):
    number = 10**9+7
    n_q = 0
    idx_list = []
    for i in range(len(string)):
        if string[i]=="?":
            n_q+=1
            idx_list.append(i)
    res = 0
    for j in range(2**n_q):
        new = get_bin(j,n_q)
        str_list = list(string)
        for i in range(n_q):
            str_list[idx_list[i]] = new[i]
        fin_list = "".join(str_list)
        res += zeroOne(fin_list)
        res = res%number
    return res

sys.stdin = open("test.in")
line = sys.stdin.readlines()[0]
result = input(line)
print(result)