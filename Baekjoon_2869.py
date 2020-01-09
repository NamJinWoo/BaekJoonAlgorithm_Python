A, B, V = map(int, input().split())

limit = V - A
if limit % (A - B) == 0:
    print(int(limit / (A - B) + 1))
else:
    print(int(limit // (A - B) + 1 + 1))