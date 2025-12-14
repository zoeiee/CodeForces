'''g, c, l = map(int, input().split())

num = [g, c, l]
num.sort()

if max(g, c, l) - min(g, c, l) >= 10:
    print("check again")
else:
    print("final", num[1])'''

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
