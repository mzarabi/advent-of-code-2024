def inputLists():
    with open('day01/input.txt') as file:
        list1 = []
        list2 = []

        for line in file:
            line = line.split()
            list1.append(int(line[0]))
            list2.append(int(line[1])) 
        return list1, list2


def solution1():
    list1, list2 = inputLists()
    list1.sort()
    list2.sort()
    
    sum = 0
    for (l1, l2) in zip (list1, list2):
        sum += abs(l1-l2)

    return sum


def solution2():
    list1, list2 = inputLists()

    sum = 0
    for number in list1:
        sum += number * list2.count(number)

    return sum


print(solution1())
print(solution2())