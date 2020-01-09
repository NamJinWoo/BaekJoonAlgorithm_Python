def solution(p):
    answer = ''
    balance = 0
    # 규칙 1
    if p == '':
        return ''
    for i in range(len(p)):
        if p[i] == '(':
            balance += 1
        elif p[i] == ')':
            balance -= 1
        if balance == 0:
            # 규칙 2
            u = p[0:i+1]
            v = p[i+1:]
            # 규칙 3
            if u[0] == '(':
                answer = answer + u
                # 규칙 3-1
                answer = answer + solution(v)
                break
            else:
                # 규칙 4
                # 규칙 4-1
                answer = '('
                # 규칙 4-2
                answer = answer + solution(v)
                # 규칙 4-3
                answer = answer + ')'
                # 규칙 4-4
                u = u[1:len(u)-1]
                changed_word = ''
                for j in range(len(u)):
                    if u[j] == ')':
                        changed_word = changed_word + '('
                    else:
                        changed_word = changed_word + ')'
                # 규칙 4-5
                answer = answer + changed_word
                break

    return answer

print(solution("()))((()"))