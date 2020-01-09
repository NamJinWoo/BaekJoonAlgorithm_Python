num = int(input())

sum_list = list()
sum_list.append(0)
sum_list.append(1)
sum_list.append(2)
for i in range(3, num+1):
    sum_list.append(sum_list[i-1] + sum_list[i-2])

print(sum_list[num] % 10007)