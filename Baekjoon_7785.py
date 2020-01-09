import sys
lineCount = int(sys.stdin.readline())

d = dict()
for _ in range(lineCount):
    name, status = input().split(" ")
    if status == "enter":
        d[name] = 1
    else:
        del d[name]

keyList = list(d.keys())
keyList.sort(reverse=True)
for item in keyList:
    print(item)
