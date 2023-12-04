import re
import numpy as np

def part1(file):
    finalCount = 0
    symbols = ["#", "%", "/", "*", "&", "+", "=", "@", "-", "$"]

    with open(file, "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if len(lines) > i + 1:
                nextLineShort = lines[i+1]
            if i > 0:
                previousLineShort = lines[i-1]
            match = re.findall(r"\d\d?\d?", line)
            for k in match:
                working = 0
                found = line.find(k)
                if i == 0 and found == 0:
                    if line[len(k)] in symbols:
                        working = 1
                    if len(lines) > i + 1:
                        for m in range(0, len(k) + 1):
                            if nextLineShort[m] in symbols:
                                working = 1
                elif i > 0 and found == 0 :
                    if len(lines) > i + 1:
                        for m in range(0, len(k) + 1):
                            if nextLineShort[m] in symbols:
                                working = 1
                    if line[len(k)] in symbols:
                        working = 1 
                    for m in range(0, len(k) + 1):
                        if previousLineShort[m] in symbols:
                            working = 1
                elif i == 0 and found > 0 :
                    if len(lines) > i + 1:
                        for m in range(found - 1, found + len(k) + 1):
                            if nextLineShort[m] in symbols:
                                working = 1
                    if line[found + len(k)] in symbols or line[(found - 1)] in symbols:
                        working = 1
                elif i > 0 and found > 0 :
                    if len(lines) > i + 1:
                        for m in range(found - 1, found + len(k) + 1):
                            if nextLineShort[m] in symbols:
                                working = 1
                    if line[found + len(k)] in symbols or line[(found - 1)] in symbols:
                        working = 1
                    for m in range(found - 1, found + len(k) + 1):
                        if previousLineShort[m] in symbols:
                            working = 1
                
                line = line[found + len(k):]
                if len(lines) > i + 1:
                    nextLineShort = nextLineShort[found + len(k):]
                if i > 0:
                    previousLineShort = previousLineShort[found + len(k):]
                
                finalCount = finalCount + int(k) if working == 1 else finalCount

    print("finalCount:", finalCount)

def part2(file):
    finalCount = []
    finalCountTwo = []
    added = 0
    n = 1
    x = 1
    symbols = [48,49,50,51,52,53,54,55,56,57]
    
    with open(file, "r") as file:
        lines = file.readlines()
        arr = np.zeros((len(lines), len(lines[0])))
        for i in range(len(lines)):
            line = lines[i]
            for k, m in enumerate(line):
                arr[i, k] = ord(m)
        print(arr)
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if arr[i][j] == 42:
                    if i != 0:
                        if arr[i-1][j-1] in symbols and arr[i-1][j] in symbols and arr[i-1][j+1] in symbols:
                            finalCount.append(chr(int(arr[i-1][j-1])))
                            finalCount.append(chr(int(arr[i-1][j])))
                            finalCount.append(chr(int(arr[i-1][j+1])))
                            added = 1
                            print("hier", finalCount, finalCountTwo)
                        for m in range(3):
                            print("M:", m)
                            if arr[i-1][j-1+m] in symbols:
                                if x <= 1:
                                    while arr[i-1][j+m-n] in symbols:
                                        #print("this should run once")
                                        finalCount.append(chr(int(arr[i-1][j+m-n])))
                                        n = n+1
                                if n != 1:
                                    while arr[i-1][j+m+x] in symbols:
                                        finalCountTwo.append(chr(int(arr[i-1][j+m+x])))
                                        x = x+1
                                print("hier", finalCount, finalCountTwo, added)
                        n = 1
                        x = 1
                        if finalCount != [] or finalCountTwo != []:
                            pass
                        else:
                            pass
                        if arr[i][j-1] in symbols:
                            while arr[i][j-n] in symbols:
                                #print("this should run once")
                                finalCount.append(chr(int(arr[i-1][j-n])))
                                n = n+1
                        if arr[i][j+1] in symbols: 
                            while arr[i-1][j+x] in symbols:
                                finalCountTwo.append(chr(int(arr[i-1][j+x])))
                                x = x+1
    def cleanupLists(listReversed, list):
        listReversed.reverse()
        for i in range(len(listReversed)):
            finalInt = int(str(finalInt + "" + i))
        for k in range(len(list)):
            finalIntTwo = int(str(finalIntTwo + "" + i))



#part1("input.txt")
part2("input.txt")