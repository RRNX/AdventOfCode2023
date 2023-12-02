import re
finalCount = 0
file = open("input.txt")

for line in file: 
    lineParam = line.split(": ", 1)
    gameCount = lineParam[0].removeprefix("Game ")
    currentString = lineParam[1].split(";")
    invalid = 0
    for i in currentString:
        #print(i)
        redInt = 0
        foundRed = i.find("red")
        #print("index:", found)
        #print("Found char:", i[found-2])
        if foundRed != -1:
            if i[foundRed-3] and ord(i[foundRed-3]) > 48 and ord(i[foundRed-3]) <= 57:
                redInt = int(i[foundRed-3] + "" + i[foundRed-2])
                #print("redInt:", redInt)
            else:
                redInt = int(i[foundRed-2])
                #print("redInt:", redInt)

        blueInt = 0
        foundBlue = i.find("blue")
        #print("index:", found)
        #print("Found char:", i[found-2])
        if foundBlue != -1:
            if i[foundBlue-3] and ord(i[foundBlue-3]) > 48 and ord(i[foundBlue-3]) <= 57:
                blueInt = int(i[foundBlue-3] + "" + i[foundBlue-2])
                #print("redInt:", redInt)
            else:
                blueInt = int(i[foundBlue-2])
                #print("redInt:", redInt)

        greenInt = 0
        foundGreen = i.find("green")
        #print("index:", found)
        #print("Found char:", i[found-2])
        if foundGreen != -1:
            if i[foundGreen-3] and ord(i[foundGreen-3]) > 48 and ord(i[foundGreen-3]) <= 57:
                greenInt = int(i[foundGreen-3] + "" + i[foundGreen-2])
                #print("redInt:", redInt)
            else:
                greenInt = int(i[foundGreen-2])
                #print("redInt:", redInt)

        #redInt += redInt
        #blueInt += blueInt
        #greenInt += greenInt
        #print("redInt:", redInt)
        #print("blueInt:", blueInt)
        #print("greenInt:", greenInt)
        if redInt > 12 or greenInt > 13 or blueInt > 14:
            invalid = 1
        redInt, blueInt, greenInt = 0, 0, 0
        

        
        # test = [m.start() for m in re.finditer("\d\sred", line)]
        # print(test)
        #redCount =  redCountChar[0].split(" red", 1) if redCountChar else 0
        #if redCountChar: del redCount[1]
        #testCount =
        #print("redCount:", redCountChar)

    #print(gameCount)
    if invalid == 0:
        print(gameCount, "is valid")
        finalCount += int(gameCount)
print("finalCount:", finalCount)
    