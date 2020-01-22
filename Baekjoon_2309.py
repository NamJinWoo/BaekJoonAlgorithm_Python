from itertools import combinations

h_list = list()
for _ in range(9):
    h_list.append(int(input()))

final_list = list()
for item in list(combinations(h_list,7)):
    if sum(list(item)) == 100:
        final_list = list(item)
        break
final_list.sort()
for i in final_list:
    print(i)

# print(list(map(sum, list(combinations(list_1,2)))))
