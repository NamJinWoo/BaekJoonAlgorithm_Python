while True:
    x, y = input().split( )
    if int(x) == 0 and int(y) == 0:
        break
    elif int(x) % int(y) == 0:
        print("multiple")
    elif int(y) % int(x) == 0:
        print("factor")

    else:
        print("neither")