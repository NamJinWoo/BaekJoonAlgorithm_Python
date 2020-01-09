import operator
N, C = map(int, input().split())
line = input().split()
d = dict()
for item in line:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1

sorted_list = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
result_list = []
for item in sorted_list:
    result_list.extend([item[0]]*item[1])
print(*result_list)

