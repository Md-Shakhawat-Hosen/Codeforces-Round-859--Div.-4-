t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    r = a + b
    r2 = a - b
    if r == c:
        print('+')
    elif r2 == c:
        print('-')