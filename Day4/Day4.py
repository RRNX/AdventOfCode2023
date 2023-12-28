import re

def part1(input):
	with open(input, "r") as file:
		lines = file.readlines()
		for i in range(len(lines)):
			line = lines[i]
			lineParam = line.split(": ", 1)
			finalInt = 0
			finalList = []
			totalWinningNumbers = 0
			CardCount = int(lineParam[0].removeprefix("Card "))
			currentString = lineParam[1].split(" | ")
			match = re.findall(r"\d\d?", currentString[0])
			ownNumbers = match
			match = re.findall(r"\d\d?", currentString[1])
			winningNumbers = match
			for j in range(len(ownNumbers)):
				if ownNumbers[j] in winningNumbers:
					totalWinningNumbers = totalWinningNumbers + 1
			if totalWinningNumbers >= 1:
				finalInt = 1
			for j in range(totalWinningNumbers - 1):
				finalInt *= 2
			finalList.append(finalInt)
		
def part2(input, output):
	totalWinningLines = 1
	with open(input, "r") as file:
		totalWinningLines = 0
		lines = file.readlines()
		for i in range(len(lines)):
			line = lines[i]
			lineParam = line.split(": ", 1)
			totalWinningNumbers = 0
			currentString = lineParam[1].split(" | ")
			match = re.findall(r"\d\d?", currentString[0])
			ownNumbers = match
			match = re.findall(r"\d\d?", currentString[1])
			winningNumbers = match
			for j in range(len(ownNumbers)):
				if ownNumbers[j] in winningNumbers:
					totalWinningNumbers = totalWinningNumbers + 1
			if totalWinningNumbers > 0: totalWinningLines = totalWinningLines + 1
			with open(output, "a") as outputFile:
				for j in range(i, totalWinningNumbers + i + 1):
					outputFile.write(lines[j])
			outputFile.close()
	with open(output, "a+") as file:
		while True:
			totalWinningLines = 0
			lines = file.readlines()
			for i in range(len(lines)):
				line = lines[i]	
				lineParam = line.split(": ", 1)
				totalWinningNumbers = 0
				currentString = lineParam[1].split(" | ")
				match = re.findall(r"\d\d?", currentString[0])
				ownNumbers = match
				match = re.findall(r"\d\d?", currentString[1])
				winningNumbers = match
				for j in range(len(ownNumbers)):
					if ownNumbers[j] in winningNumbers:
						totalWinningNumbers = totalWinningNumbers + 1
						totalWinningLines = totalWinningLines + 1
				with open(output, "a") as outputFile:
					#print("I:", i)
					for j in range(i, totalWinningNumbers + i):
						print("this i j:", j)
						outputFile.write(lines[j])
				outputFile.close()
			print("this has looped")
			if totalWinningLines == 0: break
			

#part1("input.txt")
part2("input.txt", "output.txt")