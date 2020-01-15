import datetime

def solution(lines):
    answer = 0
    start_list = []
    end_list = []
    for line in lines:
        time_tmp = line.split(" ")
        # 종료 시간을 저장합니다. 년월일 + 시간.
        end_time = "".join(time_tmp[0] + " " + time_tmp[1])
        # 지속시간을 변수에 저장합니다. 마지막 s를 제외한 모든 숫자들.
        process_t = float(time_tmp[2][:-1])

        # 모두 datetime으로 전환 해줍니다.
        end_time = datetime.datetime.fromisoformat(end_time)
        process_t = datetime.timedelta(seconds=process_t)

        # 시작시간과 종료시간을 모두 저장합니다.
        start_list.append(end_time - process_t + datetime.timedelta(seconds = 0.001))
        end_list.append(end_time)

    # 합친다.
    final_list = start_list + end_list
    # 1초라는 시간을 저장합니다.
    one_sec = datetime.timedelta(seconds=1)

    for item in final_list:
        result = 0
        for i in range(len(start_list)):
            # 한쪽만 걸쳐있거나 / 1초가 안에 포함되어있거나를 나눕니다.
            if item <= start_list[i] < item + one_sec or item <= end_list[i] < item + one_sec:
                result += 1
            elif start_list[i] <= item and end_list[i] >= item + one_sec:
                result += 1

        if answer < result:
            answer = result
    print(answer)


solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])