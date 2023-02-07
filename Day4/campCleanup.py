### I'll be honest, this isn't my best work. Might go back and optimize this


def rangeContainmentSum(pairList, part1 = False, part2 = False):
    containedCounter = 0
    for pair in pairList:
        firstRange = pair[0].split("-")
        secondRange = pair[1].split("-")
        x1, x2 = int(firstRange[0]), int(firstRange[1])
        y1, y2 = int(secondRange[0]), int(secondRange[1])

        if part1:
            if (x1 >= y1 and x2 <= y2) or (y1 >= x1 and y2 <= x2):
                print("Is a subset")
                print(firstRange)
                print(secondRange)
                containedCounter += 1
        
        elif part2:

            #[1,2] [3,4]
            if (x1 in range(y1,y2+1) or x2 in range(y1,y2+1)) or (y1 in range(x1,x2+1) or y2 in range(x1,x2+1)):
                print("Is a subset")
                print(firstRange)
                print(secondRange)
                containedCounter += 1

    return containedCounter

    

if  __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputList = f.readlines()
        f.close()
    
    formattedList = []
    for pair in inputList:
        pair = pair[:-1].split(",")
        formattedList.append(pair)
    
    print("The answer to part 1 is: "+str(rangeContainmentSum(formattedList, part1 = True)))
    print("The answer to part 2 is: "+str(rangeContainmentSum(formattedList, part2 = True)))
    print(len(formattedList))


