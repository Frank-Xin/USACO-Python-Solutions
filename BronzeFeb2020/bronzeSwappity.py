inputData = open("swap.in", "r")
outputData = open("swap.out", "w")

n, k = list(map(int,inputData.readline().split()))
cows = [i for i in range(1, n+1)]
a1, a2 = list(map(int,inputData.readline().split()))
b1, b2 = list(map(int,inputData.readline().split()))

repeat = 0

if (k <= 10000):
    for i in range(k):
        cows[a1-1: a2] = cows[a1-1: a2][::-1]
        cows[b1-1: b2] = cows[b1-1: b2][::-1]
else:
    for i in range(k):
        cows[a1-1: a2] = cows[a1-1: a2][::-1]
        cows[b1-1: b2] = cows[b1-1: b2][::-1]
        if cows == [i for i in range(1, 101)]:
            repeat = i+1
            break

    remain = k % repeat
    cows = [i for i in range(1, 101)]
    for i in range(remain):
        cows[a1-1: a2] = cows[a1-1: a2][::-1]
        cows[b1-1: b2] = cows[b1-1: b2][::-1]


for i in range(len(cows)):
    outputData.write("{}\n".format(cows[i]))

outputData.close()
inputData.close()
