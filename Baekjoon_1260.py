firstLine = input()


class Node:
    children = []

    def __init__(self, number):
        self.number = number

    def add_child(self, child):
        newNode = Node(child)
        self.children.append(newNode)


firstNumber = firstLine.split(" ")[2]
firstNode = Node(firstNumber)

for i in range(int(firstLine.split(" ")[1])):
    line = input()
    if firstNumber in line.split(" "):
        if firstNumber == line.split(" ")[0]:
            firstNode.add_child(int(line.split(" ")[1]))
        else:
            firstNode.add_child(int(line.split(" ")[0]))

print(firstNode.children)
