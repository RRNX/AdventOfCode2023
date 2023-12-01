import re
file = open("input.txt")
finalList = []
literalNumbers = ["one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9"]

for line in file:
    #print(line)
    digits = [0, 0]
    currentMax = 0
    currentMin = 100
    for elementLiteral in literalNumbers:
        test = [m.start() for m in re.finditer(elementLiteral, line)]
        #print(test)
        if test:
            for i in test:
                #print(i)
                if currentMin > i:
                    currentMin = i
                    digits[0] = round((literalNumbers.index(elementLiteral) + 1.5) / 2)
                if currentMax <= i:
                    currentMax = i
                    digits[1] = round((literalNumbers.index(elementLiteral) + 1.5) / 2)
    #print(digits)
    finalList.append(int(str(digits[0]) + "" + str(digits[1])))
    #print(digits[0])
    #print(digits[1])
    digits.clear()
    
    
    
    #print("currentMax:", currentMax)
    #print("currentMin:", currentMin)
        # indexInLine = line.find(elementLiteral)
        # print("searching", elementLiteral)
        # if indexInLine != -1:
        #     indexInLineMax = indexInLine if indexInLineMax < indexInLine else indexInLineMax
        #     indexInLineMin = indexInLine if indexInLineMin > indexInLine else indexInLineMin
        #     digits_before.insert(indexInLine, literalNumbers.index(elementLiteral) // 2)
    #print(firstDigit, lastDigit)
    #digits = [x for x in digits_before if x != '']
    #print(digits_before)
    #print(digits[0], digits[len(digits) -1 ])
    #print("\n\n")
    #digits_before = []
    #digits = []
    #indexInLineMax = 0
#for i in finalList:
#    print(i)
print(len(finalList))
print(sum(finalList))

#print("Final sum: "sum(finalList))
# 