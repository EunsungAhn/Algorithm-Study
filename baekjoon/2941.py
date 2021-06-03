croatiaAlphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
for ca in croatiaAlphabet:
    word = word.replace(ca, '*')

print(len(word))