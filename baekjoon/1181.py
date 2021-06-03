N = int(input())

wordSet = set()
for i in range(N):
    word = input()
    wordSet.add((len(word), word))

wordList = sorted(wordSet)
for i in range(len(wordList)):
    print(wordList[i][1])