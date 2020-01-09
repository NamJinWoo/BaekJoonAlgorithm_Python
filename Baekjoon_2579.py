stairs = int(input())

stairs_list = list()
score_list = list()
stairs_list.append(0)
score_list.append(0)

for _ in range(stairs):
    stairs_list.append(int(input()))

score_list.append(stairs_list[1])
score_list.append(stairs_list[1] + stairs_list[2])
score_list.append(max(stairs_list[1] + stairs_list[3], stairs_list[2] + stairs_list[3]))

for i in range(4, stairs+1):
    score_list.append(max(stairs_list[i]+score_list[i-2], stairs_list[i] + stairs_list[i-1] + score_list[i-3]))

print(score_list[-1])
