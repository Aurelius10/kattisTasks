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
    result = 0
    for j in range(2**n_q):
        new = get_bin(j,n_q)
        str_list = list(string)
        for i in range(n_q):
            str_list[idx_list[i]] = new[i]
        fin_list = "".join(str_list)
        result += zeroOne(fin_list)
        if result > number:
            result = result%number
    print(result)

def sum_list(list):
    res=0
    for el in list:
        res += el + 1
    return res
def nCr(x, y):
    return int(math.factorial(x)/(math.factorial(y)*math.factorial(x-y)))

def teller(string):
    number = 10**9+7
    count0=0
    count1=0
    count_spm=0
    idx_0= []
    idx_1 = []
    idx_spm = []
    length = len(string)
    for i in range(length):
        if string[i]=="0":
            count0+=1
            idx_0.append(i)
        elif string[i]=="1":
            count1+=1
            idx_1.append(i+1)
        else:
            count_spm+=1
            idx_spm.append(i+1)
    res = (sum_list(idx_0)-add(count0))*2**count_spm

    for index_spm in idx_spm:
        res += index_spm*2**(count_spm-1)
    counter = 1
    for i in range(1, count_spm+1):
        factor = nCr(count_spm, i)
        res -= (count0 + i) * (2**(count_spm)-counter)
        counter += factor
    res = res%number
    print(res)

def teller_test1(string):
    number = 10**9+7
    count0=0
    count1=0
    count_spm=0
    idx_0= []
    idx_1 = []
    idx_spm = []
    length = len(string)
    for i in range(length):
        if string[i]=="0":
            count0+=1
            idx_0.append(i)
        elif string[i]=="1":
            count1+=1
            idx_1.append(i+1)
        else:
            count_spm+=1
            idx_spm.append(i+1)
    factor1 = (2**count_spm)%number
    res = (sum_list(idx_0)-add(count0+count_spm-1))*factor1
    res = res%number
    factor2 = (2**(count_spm-1))%number
    for index_spm in idx_spm:
        res += index_spm*factor2
        res = res%number
    counter = 1
    for i in range(1, count_spm):
        res += (count0 + i) * counter
        res = res%number
        counter += nCr(count_spm,i)
    res -= (count0 + count_spm)
    res = res%number
    print(res)

import random
string=""
for i in range(40):
    rand = random.random()
    if rand < 0.3:
        string = string+"0"
    elif rand < 0.7:
        string = string+"1"
    else:
        string = string+"?"
print(string)

import time
t = time.time()
teller(string)
print("elpased1:", time.time()-t)
t = time.time()
input(string)
print("elpased2:", time.time()-t)

#for i in sys.stdin:
#    print(input(string=i))