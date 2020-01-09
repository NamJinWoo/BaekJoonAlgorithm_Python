# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 최종적으로 1을 만들어라.

num = int(input())
cal_list = [num]
count = 0

while True:
    if 1 in cal_list:
        print(count)
        break
    r_list = list()
    for item in cal_list:
        if item % 3 == 0:
            r_list.append(item/3)
        if item % 2 == 0:
            r_list.append(item/2)
        r_list.append(item-1)
    cal_list = r_list
    count += 1
