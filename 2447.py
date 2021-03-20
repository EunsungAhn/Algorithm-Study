import sys
input = sys.stdin.readline

def makeResult(stars):
    newStars = []
    for i in range(3 * len(stars)):
        if i // len(stars) == 1:
            newStars.append(stars[i % len(stars)] + " " * len(stars) + stars[i % len(stars)])
        else:
            newStars.append(stars[i % len(stars)] * 3)
    return newStars
            

stars = ["***", "* *", "***"]
N = int(input())
power = 1
while N != 3:
    N //= 3
    power += 1
    
for i in range(power - 1):
    stars = makeResult(stars)
for i in stars:
    print(i)