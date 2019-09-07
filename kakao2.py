
def solution(p):
    answer = ''
    balance = 0
    isBalanced = True
    for i in range(len(p)):
        if p[i] == '(':
            balance += 1
        elif p[i] == ')':
            balance -= 1
        if balance == 0:
            u = p[0:i+1]
            v = p[i+1:]
            if u[0] == '(':
                answer = answer + u
                answer = answer + solution(v)
                break
            else:
                answer = '('
                answer = answer + solution(v)
                answer = answer + ')'
                u = u[1:len(u)-1]
                changed_word = ''
                for j in range(len(u)):
                    if u[j] == ')':
                        changed_word = changed_word + '('
                    else:
                        changed_word = changed_word + ')'
                answer = answer + changed_word
                break

    return answer

print(solution("()))((()"))