N = int(input())

if N == 1:
    print('1')
else:
    i = 0
    while True:
        #print(i)
        if 1 + 3*i*(i+1) < N and N <= 1 + 3*(i+1)*(i+2):
            print(i+2)
            break
        i += 1