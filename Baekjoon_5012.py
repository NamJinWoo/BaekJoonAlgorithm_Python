import sys

n = int(sys.stdin.readline())
num_list = [int(num) for num in sys.stdin.readline().split()]

result = 0
for i in range(n):
    for j in range(i+1, n):
        if num_list[i] > num_list[j]:
            for k in range(j+1, n):
                if num_list[j] > num_list[k]:
                    result += 1

print(result)