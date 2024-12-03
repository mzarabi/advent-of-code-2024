import re

matchingPattern = r"mul\((\d+),(\d+)\)"

def inputString():
    with open('day03/input.txt') as file:
        return file.read()
    

def solution1 (inputString):
    matches = re.findall(matchingPattern, inputString)
    return sum(int(a) * int(b) for a, b in matches)


def solution2 (inputString):
    splitPattern = r"(do\(\)|don't\(\))"
    rows = re.split(splitPattern, inputString)
    
    enabled = True
    totalSum = 0
    for row in rows:
        if row == "do()":
            enabled = True
        elif row == "don't()":
            enabled = False
        if enabled:
            matches = re.findall(matchingPattern, row)
            totalSum += sum(int(a) * int(b) for a, b in matches)
    return totalSum


print(solution1(inputString()))
print(solution2(inputString()))