def main():
    first_line = input()
    countries = first_line.split(" ")
    # 나라를 저장한다.
    result_dict = dict()

    for i in range(6):
        A, B, W, D, L = input().split(" ")
        calculate(result_dict, A, B, W, D, L)

    for result_key in result_dict.keys():
        print("{0:.10f}".format(result_dict[result_key]))


def calculate(result_dict, A, B, W, D, L):
    # 승률을 더해준다.
    if A in result_dict:
        result_dict[A] = result_dict[A] + 3*float(W) + 1*float(D)
    else:
        result_dict[A] = 3*float(W) + 1*float(D)

    if B in result_dict:
        result_dict[B] = result_dict[B] + 3*float(L) + 1*float(D)
    else:
        result_dict[B] = 3*float(L) + 1*float(D)

main()