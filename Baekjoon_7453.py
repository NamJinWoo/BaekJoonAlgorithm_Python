import sys
A = []
B = []
C = []
D = []

lineCount = int(sys.stdin.readline())
AB = []
CD = []
for _ in range(lineCount):
    a1, b1, c1, d1 = map(int, sys.stdin.readline().split(" "))
    A.append(a1)
    B.append(b1)
    C.append(c1)
    D.append(d1)

for i in range(lineCount):
    for j in range(lineCount):
        AB.append(A[i]+B[j])
        CD.append(C[i]+D[j])

result = 0
AB.sort()
CD.sort()
print(AB)
print(CD)

if len(AB) == len(set(AB)):
    AB = set(AB)
    CD = set(CD)
    for i in AB:
        if -i in CD:
            result += 1
else:
    for i in AB:
        start = 0
        end = len(CD) - 1
        while start <= end:
            mid = (start + end) // 2
            if CD[mid] == -i:
                result += 1
                break
                # 함수를 끝내버린다.
            elif CD[mid] < -i:
                start = mid + 1
            else:
                end = mid - 1

print(result)
