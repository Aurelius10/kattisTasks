import sys
import math
sys.stdin = open("test.in")

def pos(num):
        if num == 1:
                return 0, 0
        check1 = int(math.sqrt(num))
        sq = check1*check1
        if check1%2==0:
                x = -int(check1/2) + 1
                y = int(check1/2)
                if check1**2 == num:
                        return x, y
                else:
                        if num - sq > check1:
                                x += num - sq - check1 - 2
                                y -= check1
                        else:
                                x -= 1
                                y -= num - sq - 1  
        else:
                x = int(check1/2)
                y = -x
                if check1**2 == num:
                        return x, y
                else:
                        if num - sq > check1:
                                x -= num - sq - check1 - 2
                                y += check1
                        else:
                                x += 1
                                y += num - sq - 1  
        return x, y
def number(x, y):
        num=1
        if abs(y) >= abs(x):
                if y > 0:
                        num += 3*y
                        for i in range(y-1):
                                num += 8*(i+1)
                        num -= x
                else:
                        y = abs(y)
                        num += 7*y
                        for i in range(y-1):
                                num += 8*(i+1)
                        num += x
        else:
                if x > 0:
                        num += x
                        for i in range(x-1):
                                num += 8*(i+1)
                        num += y
                else:
                        x = abs(x)
                        num += 5*x
                        for i in range(x-1):
                                num += 8*(i+1)
                        num -= y

        return num

def check_prime(num):
        if num==2:
                return True
        if num%2==0:
                return False
        if num==1:
                return False
        s_num = int(math.sqrt(num))
        if s_num%2==0:
                s_num -= 1
        for i in range(s_num, 1, -2):
                if num%i == 0:
                        return False
        return True

def check_next_neighbor(x, y, x_p, x_l, y_l, x_b, y_b):
        for y_temp in range(y-1, y+2):
                if y_temp < y_l or y_temp > y_b:
                        continue
                else:
                        if check_prime(number(x+x_p, y_temp)):
                                res_x.append(x+x_p)
                                res_y.append(y_temp)
                                res_x2, res_y2 = check_next_neighbor(x+x_p, y_temp, x_p, x_l, y_l, x_b, y_b)


def enclosed(x, y):
        if not check_prime(number(x-1,y)):
               return False
        if not check_prime(number(x+1,y)):
               return False
        if not check_prime(number(x,y-1)):
               return False
        if not check_prime(number(x,y+1)):
               return False
        return True
        
#for i in sys.stdin:
num1, num2 = [22, 32]#i.split()
case = 1
x1, y1 = pos(int(num1))
x2, y2 = pos(int(num2))
if x2 >= x1:
        x_pen = 1
        x_min = x2 - x1
else:
        x_pen = -1
        x_min = x1 - x2
if y2 >= y1:
        y_pen = 1
        y_min = y2 - y1
else:
        y_pen = -1
        y_min = y1 - y2
is_possible = False
primes_x = []
primes_y = []
if enclosed(x1, y1) or enclosed(x2, y2):
        print("Case", str(case)+":", 'impossible')
        
for x in range(x1, x2+x_pen):
        for y in range(y1, y2+y_pen):
                if check_prime(number(x, y)):

                        print(x, y)
                        primes_x.append(x)
                        primes_y.append(y)
net = []
for i in range(len(primes_x)):

print("numbers:", num1, num2)
print("position:", x1, y1, ";", x2, y2)
print("min distance:", y_min+x_min)