import sys
first = True
first2 = True
counter = 0
result = []
#sys.stdin = open("problemA.in")
for i in sys.stdin:
        if first:
                first = False
                tot = int(i.split()[0])
        elif first2:
                guests = int(i.split()[0])
                first2 = False
        else:
                first2 = True
                ab = i.split()
                try:
                        for j in range(guests):
                                checker = False
                                for k in range(guests):
                                        if k != j and ab[k] == ab[j]:
                                                checker = True
                                if not checker:
                                        raise Exception()
                except Exception:
                        result.append(ab[j])
                        counter += 1
                        continue
        if counter == tot:
                break
for i in range(len(result)):
        print("Case #"+str(i+1)+":", result[i])