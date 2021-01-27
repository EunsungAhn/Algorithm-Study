N = int(input())
countGroupWord = N
for i in range(N):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    countAlphabet = [0 for i in range(26)]
    word = input()
    for j in range(len(word)):
        countAlphabet[alphabet.find(word[j])] += 1
        if countAlphabet[alphabet.find(word[j])] > 1 and word[j - 1] != word[j]:
            countGroupWord -= 1
            break
print(countGroupWord)