def solution(s):
    answer = 0
    result_array = []
    count_dict = dict( )
    gap_size = 1

    while gap_size <= len(s) / 2:
        result_string = ""
        start_point = 0
        for i in range(0, len(s), gap_size):
            start_point = i
            if start_point + gap_size <= len(s):
                if s[start_point: start_point + gap_size] == s[start_point + gap_size: start_point + (2 * gap_size)]:
                    # 연속해서 같을 때
                    if s[start_point: start_point + gap_size] in count_dict:
                        count_dict[s[start_point: start_point + gap_size]] += 1
                    else:
                        count_dict[s[start_point: start_point + gap_size]] = 1
                else:
                    # 같지 않을 때
                    if count_dict:
                        result_string = result_string + str((list(count_dict.values( ))[0] + 1)) + \
                                        list(count_dict.keys( ))[0]
                        count_dict.clear( )
                    else:
                        result_string = result_string + s[start_point: start_point + gap_size]
            else:
                result_string = result_string + s[start_point:]

        # 여기서 저장
        result_array.append(len(result_string))
        print(result_string)
        gap_size += 1
    result_array.append(len(s))
    answer = min(result_array)
    print(result_array)
    print(answer)

solution("abcabcdede")