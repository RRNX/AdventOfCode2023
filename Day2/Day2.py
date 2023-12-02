finalCount = 0
file = open("input.txt")

for line in file: 
    lineParam = line.split(": ", 1)
    gameCount = lineParam[0].removeprefix("Game ")
    currentString = lineParam[1].split(";")
    invalid = 0
    for i in currentString:
        redInt = 0
        foundRed = i.find("red")
        if foundRed != -1:
            if i[foundRed-3] and ord(i[foundRed-3]) > 48 and ord(i[foundRed-3]) <= 57:
                redInt = int(i[foundRed-3] + "" + i[foundRed-2])
            else:
                redInt = int(i[foundRed-2])

        blueInt = 0
        foundBlue = i.find("blue")
        if foundBlue != -1:
            if i[foundBlue-3] and ord(i[foundBlue-3]) > 48 and ord(i[foundBlue-3]) <= 57:
                blueInt = int(i[foundBlue-3] + "" + i[foundBlue-2])
            else:
                blueInt = int(i[foundBlue-2])

        greenInt = 0
        foundGreen = i.find("green")
        if foundGreen != -1:
            if i[foundGreen-3] and ord(i[foundGreen-3]) > 48 and ord(i[foundGreen-3]) <= 57:
                greenInt = int(i[foundGreen-3] + "" + i[foundGreen-2])
            else:
                greenInt = int(i[foundGreen-2])

        if redInt > 12 or greenInt > 13 or blueInt > 14:
            invalid = 1
        redInt, blueInt, greenInt = 0, 0, 0

    if invalid == 0:
        print(gameCount, "is valid")
        finalCount += int(gameCount)
    else:
        print(gameCount, "is not valid")

print("finalCount:", finalCount)
    