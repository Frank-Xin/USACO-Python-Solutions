with open ("word.in", "r") as fin:
    j,k = map(int,fin.readline().split())
    str1 = fin.readline()

wordList = str1.split()
with open("word.out", "w") as fout:
    while (True):
        if (len(wordList) == 0):
            break
        total = 0
        available = []
        while (total <= k and len(wordList) >= 1):
            if (len(wordList[0]) + total <= k):
                available.append(wordList[0])
                total += len(wordList[0])
                wordList.pop(0)
            else:
                break
        fout.write(" ".join(available) + "\n")

