change = 1000 - int(input())

c_list = [500, 100, 50, 10, 5, 1]
result = 0
for c in c_list:
    if change // c > 0:
        result += change // c
        change = change - c * (change // c)
        if change == 0:
            break

print(result)