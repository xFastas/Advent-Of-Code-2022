def solutionPart1(calorieList):
    largestCalorieSum = 0
    currentCalorieSum = 0

    for calories in calorieList:
        if calories == "\n":
            if currentCalorieSum > largestCalorieSum:
                largestCalorieSum = currentCalorieSum
            currentCalorieSum = 0
        
        else:
            currentCalorieSum += int(calories)
    
    return(largestCalorieSum)


def solutionPart2(calorieList):
    calorieSumList = []
    currentCalorieSum = 0

    for calories in calorieList:
        if calories == "\n":
            calorieSumList.append(currentCalorieSum)
            currentCalorieSum = 0
        else:
            currentCalorieSum += int(calories)
    
    calorieSumList.sort(reverse=True)
    return(sum(calorieSumList[0:3]))


if  __name__ == "__main__":

    with open("calorie.txt", "r") as f:
        calorieList = f.readlines()
        f.close()
    
    solution1 = solutionPart1(calorieList)
    print("The largest calorie group is: "+str(solution1))

    solution2 = solutionPart2(calorieList)
    print("The sum of the top 3 calorie groups are: "+str(solution2))

