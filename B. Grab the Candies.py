t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    even = 0
    odd = 0
    for i in range(n):
        if li[i] % 2 == 0:
            even = even + li[i]
        else:
            odd = odd + li[i]
    if even > odd:
        print("YES")
    else:
        print("NO")
