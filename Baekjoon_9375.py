# 테스트 케이스 수
testCase = int(input())

for _ in range(testCase):
    clothCount = int(input())
    d = dict()
    for a in range(clothCount):
        name, category = input().split(" ")
        if category in d:
            d[category] += 1
        else:
            d[category] = 1

    valueList = list(d.values())
    # print(valueList)
    result = 1
    for value in valueList:
        result = result * (value+1)
    # 알몸인 경우
    result -= 1
    print(result)
