import sys
import math

def add(x):
    return int((x+1)*x/2)

def nCr_list_n2(num):
    res_list = []
    meas = int(num/2 + 0.5)
    res_list = [0]*(meas+1)
    res_list[0] = 1
    for i in range(1, meas+1):
        res_list[i] = res_list[i-1]*(num+1-i)//i
    return res_list

def nCr_list_test(num):
    res_list = []
    meas = int(num/2 + 0.5)
    res_list.append(1)
    for i in range(1, meas+1):
        factor = (num+1-i)//i
        res_list.append((res_list[i-1]*factor))
    return res_list

def nCr_list_n1(num):
    res_list = []
    meas = num/2 + 0.5
    alpha_list = []
    t = time.time()
    alpha = math.factorial(num)
    alpha_list.append(1)
    alpha_list.append(1)
    for i in range(2, num-1):
        alpha_list.append(alpha_list[i-1]*i)
    print("tester:", time.time() - t)
    i = 2
    res_list.append(1)
    res_list.append(num)
    while i < meas:
        res_list.append(alpha//(alpha_list[i]*alpha_list[num-i]))
        i += 1
    return res_list

def nCr_n(x, y, al):
    return al//(math.factorial(y)*math.factorial(x-y))

def nCr_list_n(num, al):
    res_list = []
    meas = num/2 + 0.5
    i = 0
    while i < meas:
        res_list.append(nCr_n(num, i, al))
        i += 1
    return res_list

def nCr(x, y):
    return math.factorial(x)//(math.factorial(y)*math.factorial(x-y))

def nCr_list(num):
    res_list = []
    meas = num/2 + 0.5
    i = 0
    while i < meas:
        res_list.append(nCr(num, i))
        i += 1
    return res_list

def teller4(string):
    t = time.time()
    number = 10**9+7
    count0=0
    count_spm=0
    sum0 = 0
    sumS = 0
    for i in range(len(string)):
        if string[i]=="0":
            count0+=1
            sum0 += i+1
        elif string[i] == "?":
            count_spm+=1
            sumS += i+1
    fac1 = (2**count_spm)%number
    res = (sum0-add(count0))*fac1
    fac2 = (2**(count_spm-1))
    res += sumS*fac2%number
    print("Interval1:", time.time()-t)
    t = time.time()
    if count_spm == 0:
        return int(res)
    elif count_spm == 1:
        res -= (count0+1) 
        return int(res)
    else:
        fac3 = (count_spm)*fac2
        res -= fac3*(count0+1)
        res -= (count_spm-1)*fac3//4
        return res%number
        
def teller2(string):
    t = time.time()
    number = 10**9+7
    count0=0
    count_spm=0
    sum0 = 0
    sumS = 0
    for i in range(len(string)):
        if string[i]=="0":
            count0+=1
            sum0 += i+1
        elif string[i] == "?":
            count_spm+=1
            sumS += i+1
    fac1 = 2**count_spm
    res = (sum0-add(count0))*fac1
    fac2 = fac1//2
    res += sumS*fac2
    counter = 1
    print("Interval1:", time.time()-t)
    t = time.time()
    facs = nCr_list_n2(count_spm)
    ind = 1
    print("Interval2:", time.time()-t)
    t = time.time()
    for ind in range(1, int(count_spm/2)+1):
        res -= (count0 + ind) * (fac1 - counter)
        counter += facs[ind]
    pen = 0
    if count_spm%2==0:
        pen = 1
    if count_spm != 1:
        ind += 1
    for j in range(int(count_spm/2+0.5)):
        res -= (count0 + j + ind) * (fac1 - counter)
        counter += facs[int(count_spm/2)-j-pen]
    print("Interval3:", time.time()-t)
    res = res%number
    return res
#----------------------------------------------------------------------
def teller1(string):
    t = time.time()
    number = 10**9+7
    count0=0
    count_spm=0
    sum0 = 0
    sumS = 0
    for i in range(len(string)):
        if string[i]=="0":
            count0+=1
            sum0 += i+1
        elif string[i] == "?":
            count_spm+=1
            sumS += i+1
    fac1 = 2**count_spm
    res = (sum0-add(count0))*fac1
    fac2 = fac1//2
    res += sumS*fac2
    counter = 1
    print("Interval1:", time.time()-t)
    t = time.time()
    facs = nCr_list_n1(count_spm)
    ind = 1
    print("Interval2:", time.time()-t)
    t = time.time()
    for ind in range(1, int(count_spm/2)+1):
        res -= (count0 + ind) * (fac1 - counter)
        counter += facs[ind]
    pen = 0
    if count_spm%2==0:
        pen = 1
    if count_spm != 1:
        ind += 1
    for j in range(int(count_spm/2+0.5)):
        res -= (count0 + j + ind) * (fac1 - counter)
        counter += facs[int(count_spm/2)-j-pen]
    print("Interval3:", time.time()-t)
    res = res%number
    return res
#----------------------------------------------------------------------
def teller_old(string):
    t = time.time()
    number = 10**9+7
    count0=0
    count_spm=0
    sum0 = 0
    sumS = 0
    for i in range(len(string)):
        if string[i]=="0":
            count0+=1
            sum0 += i+1
        elif string[i] == "?":
            count_spm+=1
            sumS += i+1
    fac1 = 2**count_spm
    res = (sum0-add(count0))*fac1
    fac2 = fac1//2
    res += sumS*fac2
    counter = 1
    print("Interval1:", time.time()-t)
    t = time.time()
    alpha = math.factorial(count_spm)
    facs = nCr_list_n(count_spm, alpha)
    ind = 1
    print("Interval2:", time.time()-t)
    t = time.time()
    for ind in range(1, int(count_spm/2)+1):
        res -= (count0 + ind) * (fac1 - counter)
        counter += facs[ind]
    pen = 0
    if count_spm%2==0:
        pen = 1
    if count_spm != 1:
        ind += 1
    for j in range(int(count_spm/2+0.5)):
        res -= (count0 + j + ind) * (fac1 - counter)
        counter += facs[int(count_spm/2)-j-pen]
    print("Interval3:", time.time()-t)
    res = res%number
    return res
#----------------------------------------------------------------------
def teller_old_old(string):
    t = time.time()
    number = 10**9+7
    count0=0
    count1=0
    count_spm=0
    sum0 = 0
    idx_1 = []
    idx_spm = []
    length = len(string)
    for i in range(length):
        if string[i]=="0":
            count0+=1
            sum0 += i + 1
        elif string[i]=="1":
            count1+=1
            idx_1.append(i+1)
        elif string[i] == "?":
            count_spm+=1
            idx_spm.append(i+1)
    res = (sum0-add(count0))*2**count_spm
    for index_spm in idx_spm:
        res += index_spm*2**(count_spm-1)
    counter = 1
    print("Interval1:", time.time()-t)
    t = time.time()
    facs = nCr_list(count_spm)
    ind = 1
    print("Interval2:", time.time()-t)
    t = time.time()
    for ind in range(1, int(count_spm/2)+1):
        res -= (count0 + ind) * (2**count_spm - counter)
        counter += facs[ind]
    pen = 0
    if count_spm%2==0:
        pen = 1
    if count_spm != 1:
        ind += 1
    for j in range(int(count_spm/2+0.5)):
        res -= (count0 + j + ind) * (2**count_spm - counter)
        counter += facs[int(count_spm/2)-j-pen]
    print("Interval3:", time.time()-t)
    res = res%number
    return res
#----------------------------------------------------------------------
def teller_old_old_old(string):
    t = time.time()
    number = 10**9+7
    count0=0
    count1=0
    count_spm=0
    sum0 = 0
    idx_1 = []
    idx_spm = []
    length = len(string)
    for i in range(length):
        if string[i]=="0":
            count0+=1
            sum0 += i + 1
        elif string[i]=="1":
            count1+=1
            idx_1.append(i+1)
        elif string[i] == "?":
            count_spm+=1
            idx_spm.append(i+1)
    res = (sum0-add(count0))*2**count_spm
    print("Interval1:", time.time()-t)
    t = time.time()
    for index_spm in idx_spm:
        res += index_spm*2**(count_spm-1)
    counter = 1
    print("Interval2:", time.time()-t)
    t = time.time()
    for i in range(1, count_spm+1):
        factor = nCr(count_spm, i)
        res -= (count0 + i) * (2**(count_spm)-counter)
        #print(count0 + i, factor, counter)
        counter += factor
    print("Interval3:", time.time()-t)
    res = res%number
    return res
#------------------------------------------------------------------
import random
string=""
for i in range(1000000):
    rand = random.random()
    if rand < 0.33:
        string = string+"0"
    elif rand < 0.67:
        string = string+"1"
    else:
        string = string+"?"
#print(string)
#sys.stdin = open("test.in")
#string = sys.stdin.readlines()[0]
import time
t = time.time()
print("---teller4---")
print(teller4(string))
print("elapsed:", time.time()-t)

t = time.time()
print("---teller2---")
print(teller2(string))
print("elpased:", time.time()-t)

#t = time.time()
#print("---NEW---")
#print(teller_old(string))
#print("elapsed:", time.time()-t)