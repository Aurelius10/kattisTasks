import sys
# TASK_URL: https://open.kattis.com/problems/classy

def converter(li):
    res = 0
    for i in range(len(li)):
        if li[len(li)-i-1] == "upper":
            res += 1/(4**i)
        elif li[len(li)-i-1] == "lower":
            res -= 1/(4**i)
    return res

#sys.stdin = open('problemA.in')
lines = sys.stdin.readlines()
num_cases = int(lines[0])
line_ind = 1
i = 1
while i <= num_cases:
    num_people = int(lines[line_ind])
    line_ind += 1
    name = [""]*num_people
    res = [0]*num_people
    for j in range(0, num_people):
        name[j], cl = lines[j+line_ind].split(":")
        cl = cl.strip()[:-6]
        classes = cl.split("-")
        res[j] = converter(classes)
    sort1 = sorted(range(num_people), key=lambda k: name[k])
    alpha_n = [name[k] for k in sort1]
    alpha_r = [res[k] for k in sort1]
    sort2 = sorted(range(num_people), key=lambda k: alpha_r[k], reverse=True)
    for k in range(num_people):
        print (alpha_n[sort2[k]])
    print("="*30)
    line_ind = line_ind + num_people
    i += 1        