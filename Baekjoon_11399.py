n = int(input())
q = list(map(int, input().split()))
q.sort()

for i in range(1,n):
    q[i] = q[i] + q[i-1]
print(sum(q))