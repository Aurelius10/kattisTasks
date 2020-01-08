import sys

#sys.stdin = open('test.in')
lines = sys.stdin.readlines()
rows = int(lines[0])
word3 = ["bea","bee","owe","why","and","one","won","too","two","for","you","sea","see","eye","are"]
code3 = ["b","b","o","y","&","1","1","2","2","4","u","c","c","i","r"]
word2 = ["at","to","oh","be"]
code2 = ["@","2","o","b"]
for i in range(rows):
    string = str(lines[i+1]).lower()
    for j in range(0, len(string)):
        again = True
        if string[j:j+4] == "four":
            string = string[:j] + "4" + string[j+4:]
            again = False
        if again:
            for k in range(0,15):
                if string[j:j+3] == word3[k]:
                    string = string[:j] + code3[k] + string[j+3:]
                    again = False
                    break
        if again:
            for k in range(0,4):
                if string[j:j+2] == word2[k]:
                    string = string[:j] + code2[k] + string[j+2:]
                    break
    string = string[0].upper() + string[1:]
    print(string, end="")