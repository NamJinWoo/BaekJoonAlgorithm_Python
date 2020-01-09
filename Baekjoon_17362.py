n = int(input())

if n <= 5:
    print(n)
elif ((n-5) // 4) % 2 == 0 and (n-5) % 4 == 0:
    print(5)
elif ((n-5) // 4) % 2 == 0 and (n-5) % 4 == 1:
    print(4)
elif ((n-5) // 4) % 2 == 0 and (n-5) % 4 == 2:
    print(3)
elif ((n - 5) // 4) % 2 == 0 and (n - 5) % 4 == 3:
    print(2)
elif ((n-5) // 4) % 2 == 1 and (n-5) % 4 == 0:
    print(1)
elif ((n-5) // 4) % 2 == 1 and (n-5) % 4 == 1:
    print(2)
elif ((n-5) // 4) % 2 == 1 and (n-5) % 4 == 2:
    print(3)
elif ((n - 5) // 4) % 2 == 1 and (n - 5) % 4 == 3:
    print(4)
