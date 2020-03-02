res = []
finalres = []

with open ("photo.in", "r") as fin:
    a = fin.readline()
    a = int(a)
    n = list(map(int, fin.readline().split()))


    for i in range(1, n[0]):
        res.append([])
        cur = i
        for j in range(len(n)):
            if (j > 0):
                res[i-1].append(n[j] - cur)
            else:
                res[i-1].append(cur)
                res[i-1].append(n[j] - cur)
            cur = n[j] - cur
    for i in range(len(res)):
        count = 0
        for j in range(len(res[i])):
            if (res[i][j] < 0):
                count += 1
        if (len(set(res[i])) == len(res[i]) and res[i].count(0) == 0 and count == 0):
            finalres.append(res[i])

    finalres.sort()
with open("photo.out", "w") as fout: 
    for i in range(len(finalres[0])):
        if (i == len(finalres[0])-1):
            fout.write("{}".format(finalres[0][i]))
        else:
            fout.write("{} ".format(finalres[0][i]))
    fout.write("\n") 
    

