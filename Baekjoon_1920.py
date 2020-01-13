def BinarySearch(arr, num, low, high):
    mid = int((high+low)/2)
    if low > high:
        return 0

    if num > arr[mid]:
        return BinarySearch(arr, num, mid + 1, high)
    elif num < arr[mid]:
        return BinarySearch(arr, num, low, mid - 1)
    else:
        return 1


N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
search_list = list(map(int, input().split()))
num_list.sort()

for i in range(M):
    print(BinarySearch(num_list, search_list[i], 0, len(num_list)-1))