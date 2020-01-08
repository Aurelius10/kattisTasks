import sys

#sys.stdin = open('test.in')
lines = sys.stdin.readlines()
rows, columns = map(int, lines[0].split())
matrix = [""]*rows

for i in range(rows):
    matrix[i] = list(lines[i+1].strip())
    for j in range(columns):
        matrix[i][j] = int(matrix[i][j])

probs=int(lines[rows+1])
res = []
counter0 = 0
counter1 = 1
for l in range(probs):
    p1r, p1c, p2r, p2c = map(int, lines[rows+2+l].split())
    number = matrix[p1r-1][p1c-1]
    if number > 1:
        if number == matrix[p2r-1][p2c-1]:
            if number%2 == 0:
                res.append("binary")
            else:
                res.append("decimal")
            continue
        number = number%2

    nester = [p1r]
    nestec = [p1c]
    if number == 0:
        counter0 = counter0 + 2
        counter = counter0
    else:
        counter1 = counter1 + 2
        counter = counter1

    while True:
        if len(nester)==0:
            res.append("neither")
            break
        row = nester.pop(0)
        col = nestec.pop(0)
        if matrix[row-1][col-1] == counter:
            continue
        matrix[row-1][col-1]=counter
        if row==p2r and col==p2c:
            if number == 0:
                res.append("binary")
            else:
                res.append("decimal")
            break
        rad = [row-2, row]
        kol = [col-2, col]
        if row-1 > 0:
            if matrix[row-2][col-1]%2==number:
                nester.append(row-1)
                nestec.append(col)
        if row+1 <= rows:
            if matrix[row][col-1]%2==number:
                nester.append(row+1)
                nestec.append(col)
        if col-1 > 0:
            if matrix[row-1][col-2]%2==number:
                nester.append(row)
                nestec.append(col-1)
        if col+1 <= columns:
            if matrix[row-1][col]%2==number:
                nester.append(row)
                nestec.append(col+1)

        #for i in range(rows):
        #    print(matrix[i])
        #print("")
        
for re in res:
    print(re)