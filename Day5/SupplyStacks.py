import json

def part1(supplydict, inputList):
    for command in inputList:
        commandSplit = command[:-1].split(" ")
        amount = int(commandSplit[1])
        cfrom = commandSplit[3]
        cto = commandSplit[5]

        for i in range(amount):
            poppedCrate = supplydict[cfrom].pop(0)
            supplydict[cto].insert(0, poppedCrate)

    firstCrateList = []
    for crateRow in supplydict:
        firstCrateList.append(supplydict[crateRow][0])
    
    return firstCrateList

def part2(supplydict, inputList):
    #counter = 0
    for command in inputList:
        commandSplit = command[:-1].split(" ")
        amount = int(commandSplit[1])
        cfrom = commandSplit[3]
        cto = commandSplit[5]

        #print("Before: "+str(supplydict))
        crateList = supplydict[cfrom][:amount]
        crateList.extend(supplydict[cto])
        remainingList = supplydict[cfrom][amount:]


        supplydict[cfrom] = remainingList #supplydict[cfrom][amount:]
        supplydict[cto] = crateList

        #print("After: "+str(supplydict))
        
    #    counter += 1
    #    if counter == 5:
    #        break
    
    firstCrateList = []
    for crateRow in supplydict:
        firstCrateList.append(supplydict[crateRow][0])
    
    return firstCrateList


if  __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputList = f.readlines()
        f.close()

    with open("supplydict.json", "r") as f:
        supplydict = json.load(f)



    #WARNING: Due to key similarities, comment/uncomment one at a time


    #part1Return = "".join(part1(supplydict, inputList))
    #print("The answer to part 1 is: "+part1Return)

    part2Return = "".join(part2(supplydict, inputList))
    print("The answer to part 2 is: "+part2Return)
