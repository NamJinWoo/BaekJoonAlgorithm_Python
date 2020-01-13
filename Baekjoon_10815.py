def BinarySearch(arr, num, start, end):
    while start <= end:
        mid = (start + end) // 2
        if num < arr[mid]:
            end = mid - 1
        elif num > arr[mid]:
            start = mid + 1
        else:
            return 1
    return 0


N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
search_list = list(map(int, input().split()))
num_list.sort()

for search in search_list:
    print(BinarySearch(num_list, search, 0, N-1), end=' ')

