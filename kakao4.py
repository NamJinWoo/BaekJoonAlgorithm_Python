import re

def solution(words, queries):
    answer = []
    for query in queries:
        count = 0
        regex_txt = '^'
        for s in query:
            if s == '?':
                regex_txt = regex_txt + '[a-z]'
            else:
                regex_txt = regex_txt + s
        regex_txt = regex_txt + '$'
        for word in words:
            x = re.search(regex_txt, word)
            if x:
                count += 1
        answer.append(count)
    print(answer)


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])