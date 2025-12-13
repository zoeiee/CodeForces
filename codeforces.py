g, c, l = map(int, input().split())

num = [g, c, l]
num.sort()

if max(g, c, l) - min(g, c, l) >= 10:
    print("check again")
else:
    print("final", num[1])
