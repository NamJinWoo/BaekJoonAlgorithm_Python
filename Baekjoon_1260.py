firstLine = input()


class Node:
    children = []

    def __init__(self, number):
        self.number = number

    def add_child(self, child):
        newNode = Node(child)
        self.children.append(newNode)


firstNumber = firstLine.split(" ")[0]
firstNode = Node(firstNumber)

for i in range(int(firstLine.split(" ")[1])):
    line = input()
    if firstNumber in line.split(" "):
        if firstNumber == line.split(" ")[0]:
            firstNode.add_child(int(line.split(" ")[1]))
        else:
            firstNode.add_child(int(line.split(" ")[0]))

# print(firstNode.children)
matrix = [[0]*(int(firstNumber)+1) for _ in range(int(firstNumber)+1)]
print(matrix)
