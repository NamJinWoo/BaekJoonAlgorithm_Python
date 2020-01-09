day = int(input())
car_list = list(map(int, input().split()))
result = 0
for car in car_list:
    if car == day:
        result += 1

print(result)