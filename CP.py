'''g, c, l = map(int, input().split())

num = [g, c, l]
num.sort()

if max(g, c, l) - min(g, c, l) >= 10:
    print("check again")
else:
    print("final", num[1])

t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())

    if (1 <= a <= 10 and 1 <= b <= 10 and 1 <= c <= 10 and 1 <= d <= 10 ):
        if a == b == c == d:
            print("YES")

        else:
            print("No")
    else:
        print("Error")

t = int(input())
for _ in range(t):
    n = int(input())
    a = int(input())
    liar_found = False
    for i in range(n-1):
        if a[i] == 0 and a[i+1] == 0:
            liar_found = True
            break
    if liar_found:
        print("YES")
    else:
        print("NO")'''

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))

    found = False
    for i in range(n - 1):
        if a[i] == 0 and a[i + 1] == 0:
            print("YES")
            found = True
            break

    if not found:
        print("NO")


