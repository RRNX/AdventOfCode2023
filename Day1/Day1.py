import re
file = open("input.txt")
finalList = []
literalNumbers = ["one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9"]

for line in file:
    digits = [0, 0]
    currentMax = 0
    currentMin = 100
    for elementLiteral in literalNumbers:
        found = [m.start() for m in re.finditer(elementLiteral, line)]
        if found:
            for i in found:
                #print(i)
                if currentMin > i:
                    currentMin = i
                    digits[0] = round((literalNumbers.index(elementLiteral) + 1.5) / 2)
                if currentMax <= i:
                    currentMax = i
                    digits[1] = round((literalNumbers.index(elementLiteral) + 1.5) / 2)
    finalList.append(int(str(digits[0]) + "" + str(digits[1])))
    digits.clear()

print(len(finalList))
print(sum(finalList))