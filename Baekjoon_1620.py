import sys

N, M = map(int, sys.stdin.readline().split())
d_name = dict()
d_num = dict()
for i in range(int(N)):
    name = sys.stdin.readline().rstrip()
    d_name[name] = i+1
    d_num[i+1] = name

for _ in range(int(M)):
    question = sys.stdin.readline().rstrip()
    if question.isdigit():
        print(d_num[int(question)])
    else:
        print(d_name[question])
