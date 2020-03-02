inputData = open("breedflip.in", "r")
outputData = open("breedflip.out", "w")

n = inputData.readline()
n = int(n)
strA = inputData.readline()
strB = inputData.readline()
difference = []

for i in range(n):
    if strA[i] != strB[i]:
        difference.append(i) 

dtemp = [(i-j) for i, j in enumerate(difference)]
dlength = len(set(dtemp))
        
outputData.write("{}\n".format(dlength))
inputData.close()
outputData.close()
