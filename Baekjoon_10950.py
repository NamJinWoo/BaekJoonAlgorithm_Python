lineCount = input()
for i in range(int(lineCount)):
    inputLine = input()
    firstNumber = int(inputLine.split(" ")[0])
    secondNumber = int(inputLine.split(" ")[1])
    print(firstNumber + secondNumber)
