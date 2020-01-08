import sys
import math
# TASK_URL: https://open.kattis.com/problems/sequences

def add(x):
    return int((x+1)*x/2)

def teller(string):
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
    if count_spm == 0:
        return int(res)
    elif count_spm == 1:
        res -= (count0+1) 
        return int(res)
    else:
        fac3 = (count_spm)*fac2
        res -= fac3*(count0+1)
        res -= (count_spm-1)*fac3//4
    res = res%number
    return res

#string = sys.stdin.readlines()[0]
string = "001??0"
print(teller(string))