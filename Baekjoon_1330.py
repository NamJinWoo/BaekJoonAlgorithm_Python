inputLine = input()
firstNumber = int(inputLine.split(" ")[0])
secondNumber = int(inputLine.split(" ")[1])

if firstNumber > secondNumber:
    print(">")
elif firstNumber < secondNumber:
    print("<")
else:
    print("==")
