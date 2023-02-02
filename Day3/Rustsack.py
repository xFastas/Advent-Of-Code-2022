def splitString(contentString):
    contentsLen = int(len(contentString[:-1])/2)

    return contentString[:contentsLen], contentString[contentsLen:-1]

def commonCharSum(string1, string2, string3 = ""):
    if string3 == "":
        commonChar = list((set(string1)&set(string2)))[0]
    else:
        commonChar = list((set(string1)&set(string2)&set(string3)))[0]

    if commonChar == commonChar.upper():
        return (ord(commonChar)-38)
    else:
        return (ord(commonChar) - 96)

def part1Solution(inputList):
    combinedSum = 0
    for contents in inputList:
    
        #Split the list
        firstSack, secondSack = splitString(contents)

        combinedSum += commonCharSum(firstSack, secondSack)
    
    return combinedSum

def part2Solution(inputList):
    combinedSum = 0
    sackList = []
    for contents in inputList:
        sackList.append(contents[:-1])
        if len(sackList) == 3:
            combinedSum += commonCharSum(sackList[0], sackList[1], string3 = sackList[2])
            sackList = []
    
    return combinedSum


if  __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputList = f.readlines()
        f.close()
    
    combinedSum = part1Solution(inputList)
    print("The solution to Part 1 is "+str(combinedSum))

    combinedBadgeSum = part2Solution(inputList)
    print("The solution to Part 2 is "+str(combinedBadgeSum))


        
    