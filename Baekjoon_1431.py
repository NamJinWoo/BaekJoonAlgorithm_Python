# 합을 구하는 함수
def sum(string):
    result = 0
    for s in string:
        if s.isdigit():
            result += int(s)

    return result


# 비교하는 함수
def compare(str1, str2):
    # 조건 1
    if len(str1) < len(str2):
        return True # true이면 앞에온다
    elif len(str1) > len(str2):
        return False # false이면 에온다

    # 조건 2
    if sum(str1) < sum(str2):
        return True
    elif sum(str1) > sum(str2):
        return False

    # 조건 3
    for i in range(len(str1)):
        if ord(str1[i]) < ord(str2[i]):
            return True
        elif ord(str1[i]) > ord(str2[i]):
            return False


line_count = int(input())
result_list = []

for _ in range(line_count):
    string = input()
    if len(result_list) == 0:
        result_list.append(string)
    else:
        for s in range(len(result_list)):
            # print(result_list)
            if compare(string, result_list[s]):
                result_list.insert(s, string)
                break
            else:
                if s == len(result_list)-1:
                    result_list.append(string)
                else:
                    continue

for s in result_list:
    print(s)