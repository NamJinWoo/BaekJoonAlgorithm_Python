from collections import deque


def dfs(graphDict, start_node):
    visit = list()
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            if node in graph:
                tempList = list(set(graphDict[node]) - set(visit))
                tempList.sort(reverse=True)
                stack.extend(tempList)
    return " ".join(str(i) for i in visit)


def bfs(graphDict, start_node):
    visit = list()
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            if node in graph:
                tempList = list(set(graphDict[node]) - set(visit))
                tempList.sort()
                queue.extend(tempList)

    return " ".join(str(i) for i in visit)


graph = dict()
firstLine = input().split(' ')
nodeCount, lineCount, startNode = [int(i) for i in firstLine]
for i in range(lineCount):
    line = input().split(' ')
    n1, n2 = [int(j) for j in line]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(dfs(graph, startNode))
print(bfs(graph, startNode))
