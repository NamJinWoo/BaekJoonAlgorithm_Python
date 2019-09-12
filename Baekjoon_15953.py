list_one = [10, 10, 10, 10, 10, 10, 30, 30, 30, 30, 30, 50, 50, 50, 50, 200, 200, 200, 300, 300, 500]
list_two = [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 64, 64, 64, 64, 64, 64, 64, 64, 128, 128, 128, 128, 256, 256, 512]

T = int(input())
for i in range(T):
    first, second = input().split(" ")
    total = 0
    if 1 <= int(first) <= len(list_one):
        total += list_one[len(list_one)-int(first)]
    if 1 <= int(second) <= len(list_two):
        total += list_two[len(list_two)-int(second)]
    print(total*10000)

# 배열말고 할 수 있는 방법을 생각해보자.