n = int(input())

# 시간복잡도를 생각해야할듯
default_list = [0, 1, 1]
for i in range(3, n+1):
    default_list.append(default_list[i-1] + default_list[i-2])

print(default_list[-1])
