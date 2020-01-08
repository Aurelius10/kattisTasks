import sys
# TASK_URL: https://open.kattis.com/problems/imageprocessing

#sys.stdin = open("test.in")
first = True
counter = 0
matrise = []
kernel = []
kernel_c = []
for i in sys.stdin:
        line = i.split()
        if first:
                height = int(line[0])
                width = int(line[1])
                k_height = int(line[2])
                k_width = int(line[3])
                first = False
        else:
                if counter < height:
                        matrise.append(list(map(int, line)))
                        counter += 1
                else:
                        kernel.append(list(map(int,line)))
                        kernel_c.append(list(map(int,line)))
for h in range(k_height):
        for w in range(k_width):
                kernel[h][w] = kernel_c[k_height-h-1][k_width-w-1]
for i in range(height-k_height+1):
        for j in range(width-k_width+1):
                temp = 0
                for h in range(k_height):
                        for w in range(k_width):
                                temp += matrise[i+h][j+w]*kernel[h][w]
                print(temp, end=' ')
        print(end='\n')