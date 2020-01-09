n = int(input())
stick = 64
s = 0
answer = 0

while True:
    if stick > n:
        stick = stick/2
    elif stick < n:
        if s + stick > n:
            stick = stick/2
        elif s + stick < n:
            s += stick
            stick = stick/2
            answer += 1
        else:
            answer += 1
            break
    else:
        answer += 1
        break

print(answer)