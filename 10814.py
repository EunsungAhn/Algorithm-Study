N = int(input())
memberInfo = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    memberInfo.append((age, i, name))
memberInfo = sorted(memberInfo)
for i in range(N):
    print(memberInfo[i][0], memberInfo[i][2])