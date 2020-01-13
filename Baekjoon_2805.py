N, M = map(int, input().split())
wood_list = list(map(int, input().split()))


def sumAll(n):
    s = 0
    for wood in wood_list:
        if wood - n > 0:
            s += wood - n

    return s


def BinarySearch(height):
    start = 0
    end = max(wood_list)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        s = sumAll(mid)

        if s < height:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result


print(BinarySearch(M))
