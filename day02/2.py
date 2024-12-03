def inputList():
    with open('day02/input.txt') as file:
        listOfReports = []
        for line in file:
            lst = line.split()
            b = list(map(int, lst))
            listOfReports.append(b)
        return listOfReports


def solution1(reports):
    return sum(1 for report in reports if (validReport(report)))


def solution2(reports):
    return sum(1 for report in reports if (validReport(report) or adjustReport(report)))


def validTrend(report, minDiff, maxDiff):
    for i in range(len(report) - 1):
        difference = report[i + 1] - report[i]
        if difference < minDiff or difference > maxDiff:
            return False
    return True 


def validReport(report):
    return validTrend(report,1,3) or validTrend(report, -3,-1)


def adjustReport(report):
    for i in range(len(report)):
        fixedReport = report[:i] + report[i+1:]
        if validReport(fixedReport):
            return True
    return None  


print(solution1(inputList()))
print(solution2(inputList()))