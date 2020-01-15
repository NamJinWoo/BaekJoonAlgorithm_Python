import datetime

def solution(n, t, m, timetable):
    time_dict = dict()
    timetable.sort()
    time = datetime.datetime.strptime("09:00", "%H:%M")
    # value를 m 으로 가지고 있는 dict 생성.
    for _ in range(n):
        time_dict[time.time()] = m
        time = time + datetime.timedelta(minutes=t)

    for item in timetable:
        crew_time = datetime.datetime.strptime(item, "%H:%M")
        for time in time_dict.keys():
            # 앞에 value가 0이 되면 그냥 패스. (버스가 떠남..)
            if time_dict[time] == 0:
                continue
            # key에 있는 시간보다 빠르면 한명 탑승.
            if time >= crew_time.time():
                time_dict[time] = time_dict[time] - 1
                break

        # 마지막이 0이 되면 마지막 사람보다 1분 빠른 것을 return
        if time_dict[list(time_dict.keys())[-1]] == 0:
            return (crew_time - datetime.timedelta(minutes=1)).strftime("%H:%M")
    # 아니면 버스 시간에 맞춰서 리턴.
    return list(time_dict.keys())[-1].strftime("%H:%M")
