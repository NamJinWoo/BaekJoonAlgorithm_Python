N = int(input())

factor_list = list(map(int, input().split()))
factor_list.sort()
max_num = max(factor_list)
print(factor_list[0] * factor_list[-1])