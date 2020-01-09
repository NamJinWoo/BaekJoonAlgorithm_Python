N = int(input())

word_list = list()
for _ in range(N):
    word_list.append(input())

word_set = set(word_list)

word_list_sort = list()

for word in word_set:
    word_list_sort.append((len(word), word))

word_list_sort.sort()

for word in word_list_sort:
    print(word[1])