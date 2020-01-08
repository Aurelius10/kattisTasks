import sys

sys.stdin = open('test.in')
lines = sys.stdin.readlines()
rows = int(lines[0]) + 1

def area(x1, y1, x2, y2, x3, y3):
        vec1 = [x2 - x1, y2 - y1]
        vec2 = [x3 - x1, y3 - y1]
        return abs(vec1[0]*vec2[1] - vec1[1]*vec2[0])/2

def lowest_left(v):
        res = [v[1], v[2]]
        for i in range(2, v[0]+1):
                if v[i*2] > tot_paint == 0:
                        for i in range(1, rows):
                                fig_paint = 0
                                vec = list(map(int, lines[i].split()))
                                for j in range(2, vec[0]):
                                        fig_paint += area(vec[1], vec[2], vec[2*j-1], vec[2*j], vec[2*j+1], vec[2*j+2])
                                print(fig_paint)
                                tot_paint += fig_paint
print(tot_paint)