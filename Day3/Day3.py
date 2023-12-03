import re

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
                elif i > 0 and found == 0 and working == 0:
                    if len(lines) > i + 1:
                        for m in range(0, len(k) + 1):
                            if nextLineShort[m] in symbols:
                                working = 1
                    if line[len(k)] in symbols:
                        working = 1 
                    for m in range(0, len(k) + 1):
                        if previousLineShort[m] in symbols:
                            working = 1
                elif i == 0 and found > 0 and working == 0:
                    if len(lines) > i + 1:
                        for m in range(found - 1, found + len(k) + 1):
                            if nextLineShort[m] in symbols:
                                working = 1
                    if line[found + len(k)] in symbols or line[(found - 1)] in symbols:
                        working = 1
                elif i > 0 and found > 0 and working == 0:
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

part1("input.txt")
                    