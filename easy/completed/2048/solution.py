import sys
# TASK_URL: https://open.kattis.com/problems/2048

#sys.stdin = open('test.in')
board = []
lines = sys.stdin.readlines()
board.append(lines[0].split())
board.append(lines[1].split())
board.append(lines[2].split())
board.append(lines[3].split())
board = [[int(i) for i in board2] for board2 in board]
arrow = int(lines[4])
res = [[0 for i in range(4)] for j in range(4)]

def sort_line(vec):
    i = 0
    new_vec = [0]*4
    for j in range(4):
        if vec[j] != 0:
            new_vec[i] = vec[j]
            i += 1
    j = 0
    while j < 4:
        if j != 3:
            if new_vec[j] == new_vec[j+1]:
                new_vec[j] = new_vec[j] + new_vec[j+1]
                for i in range(j+1, 3):
                    new_vec[i] = new_vec[i+1]
                new_vec[3] = 0
            else:
                new_vec[j] = new_vec[j]
        j += 1
    return new_vec

if arrow == 0:
    for i in range(4):
        res[i] = sort_line(board[i])
if arrow == 2:
    for i in range(4):
        res[i] = sort_line(board[i][::-1])[::-1]
if arrow == 1:
    line = [0]*4
    for i in range(4):
        for j in range(4):
            line[j] = board[j][i]
        line_res = sort_line(line)
        for j in range(4):
            res[j][i] = line_res[j]
if arrow == 3:
    line = [0]*4
    for i in range(4):
        for j in range(4):
            line[3-j] = board[j][i]
        line_res = sort_line(line)
        for j in range(4):
            res[3-j][i] = line_res[j]

for i in range(4):
    print(res[i][0], res[i][1], res[i][2], res[i][3])