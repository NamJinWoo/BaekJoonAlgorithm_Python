def solution(m, musicinfos):
    # #이 포함되어 있는 note 들은 다른 문자로 바꾸어 준다.
    m = m.replace('A#', 'H')
    m = m.replace('C#', 'I')
    m = m.replace('D#', 'J')
    m = m.replace('F#', 'K')
    m = m.replace('G#', 'L')
    # 생성된 tuple 들을 넣을 리스트를 생성한다.
    song_list = list()
    for musicinfo in musicinfos:
        start_time, end_time, title, note = musicinfo.split(",")
        # 시작 시간과 종료 시간을 숫자로 변환한다.
        start_hour, start_minute = map(int, start_time.split(":"))
        end_hour, end_minute = map(int, end_time.split(":"))
        # 1분당 노트 1개라는 조건을 만족시키기 위해 분 단위로 변환해준다.
        play_time = (end_hour - start_hour) * 60 + (end_minute - start_minute)

        # 처음과 같이 note 에 # 이 들어간 문자들을 바꿔준다. (동일한 조건으로 바꿔준다.)
        note = note.replace('A#', 'H')
        note = note.replace('C#', 'I')
        note = note.replace('D#', 'J')
        note = note.replace('F#', 'K')
        note = note.replace('G#', 'L')

        # play_time에 맞게 최종적으로 만들어지는 note 를 구성한다.
        final_note = note * (play_time // len(note)) + note[:play_time % len(note)]

        # 곡 제목, 최종 노트, 재생시간을 tuple 롤 만들어 list 에 넣는다.
        song_list.append((title, final_note, play_time))

    # 문제에서는 따음표가 하나 더 있지만, 답에서는 없는 것으로 처리해야 한다. 이유는 모르겠다.
    answer = "(None)"
    # 답이 여러 개가 나올 수 있기 때문에 마지막 리스트로 관리한다.
    answer_list = list()
    for song in song_list:
        # m 이 note에 포함되어 있다면,
        if m in song[1]:
            # 곡에 대한 정보를 리스트에 넣는다.
            answer_list.append(song)

    # 답이 한개라면 그것이 답이다.
    if len(answer_list) == 1:
        answer = answer_list[0][0]
    else:
        # 아니라면, play_time 을 비교한다.
        # 이렇게 하면 play_time 이 같으면 먼저 들어온 곡 제목을 출력한다는 조건 또한 맞출 수 있다.
        pt = 0
        for a in answer_list:
            if pt < a[2]:
                pt = a[2]
                answer = a[0]
    return answer
