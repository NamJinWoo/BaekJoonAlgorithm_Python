lineCount = input()
line = input()

line = list(map(int, line.split(" ")))

print('{} {}'.format(min(line), max(line)))
