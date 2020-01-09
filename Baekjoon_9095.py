testCase = int(input())

sum_list = [1,2,4]
for _ in range(4, 11):
    sum_list.append(sum(sum_list[-3:]))

for _ in range(testCase):
    print(sum_list[int(input())-1])
