word = input().upper()
includedAlphabet = list(set(word))

countList = []
for alphabet in includedAlphabet:
    count = word.count(alphabet)
    countList.append(count)

if countList.count(max(countList)) > 1:
    print('?')
else:
    maxIndex = countList.index(max(countList))
    print(includedAlphabet[maxIndex])