def solution(food_times, k):
    index = 0
    while k != 0:
        if food_times[index] != 0:
            food_times[index] -= 1
            k -= 1

        if index == len(food_times)-1:
            index = 0
        else:
            index += 1

    for i in range(index, len(food_times)):
        if food_times[i] != 0:
            return i + 1

    for i in range(0, index):
        if food_times[i] != 0:
            return i + 1

    return -1
print(solution([3,1,2], 6))
