T = int(input())

for test_case in range(1, T+1):
    # 테스트 케이스.
    n = int(input())
    # 처음 리스트.
    line_list = list(map(int,input().split()))

    total_list = list()

    # 초기에는 리스트의 맨 첫 숫자로 지정.
    prev_num = line_list[0]
    current_num = 0
    # 초기는 오름차순으로 지정.
    current_status = False
    status = ""
    sub_list = [line_list[0]]
    for i in range(1, n):
        current_num = line_list[i]

        if current_num == prev_num:
            sub_list.append(current_num)
            continue

        if not current_status and current_num > prev_num:
            current_status = True
            status = "up"
            sub_list.append(current_num)
        elif not current_status and current_num < prev_num:
            current_status = True
            status = "down"
            sub_list.append(current_num)
        elif current_status:
            if status == "up":
                if current_num > prev_num:
                    sub_list.append(current_num)
                else:
                    # total_list에 추가하고 전부 초기화.
                    total_list.append(sub_list)
                    sub_list = [current_num]
                    current_status = False
                    statusu = ""
            elif status == "down":
                if current_num < prev_num:
                    sub_list.append(current_num)
                else:
                    # total_list에 추가하고 전부 초기화.
                    total_list.append(sub_list)
                    sub_list = [current_num]
                    current_status = False
                    statusu = ""

        prev_num = current_num
    total_list.append(sub_list)

    print("#%d %d" %(test_case,len(total_list)))