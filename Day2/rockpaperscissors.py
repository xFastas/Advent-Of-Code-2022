def checkWin(opponentsChoice, yourChoice):
    winConditions = ["AY", "BZ", "CX"] #Rock is A and X, Paper is B and Y, Scissors is C and Z
    tieConditions = ["AX", "BY", "CZ"]

    if opponentsChoice+yourChoice in tieConditions:
        return 3
    
    elif opponentsChoice+yourChoice in winConditions:
        return 6
    
    else:
        return 0

def solutionPart1(rpsList):
    totalScore = 0
    SELECTIONCHART = {"X" : 1, "Y": 2, "Z": 3}
    for matchup in rpsList:
        winValue = checkWin(matchup[0], matchup[1])
        totalScore += (winValue + SELECTIONCHART[matchup[1]]) #Points for win/loss/tie + points based off your choice
    
    return totalScore

def pointsFromChoice(opponentsChoice, desiredOutcome):
    '''Determines the points you would earn based off your opponents choice and
     what your desired outcome is. For example, if the opponent chooses A (Rock) and
     the desired outcome is to win, you would play paper which is worth 2 points based
     off part 1.'''

    scissorChoice = ["AX", "BZ", "CY"]
    rockChoice = ["AY", "BX", "CZ"]

    if opponentsChoice+desiredOutcome in scissorChoice: #You want to play scissors, worth 3 points
        return 3
    
    elif opponentsChoice+desiredOutcome in rockChoice: #You want to play rock, worth 1 point
        return 1
    
    else: #You want to play paper, worth 2 points
        return 2

def solutionPart2(rpsList):
    totalScore = 0
    WINLOSETIECHART = {"X" : 0, "Y": 3, "Z": 6}
    for matchup in rpsList:
        outcomePoints = WINLOSETIECHART[matchup[1]]
        yourChoicePoints = pointsFromChoice(matchup[0], matchup[1])

        totalScore += (outcomePoints+yourChoicePoints)
    
    return totalScore



if  __name__ == "__main__":
    rpsList = []
    with open("input.txt", "r") as f:
        inputList = f.readlines()
        f.close()
    
    for column in inputList:
        column = column[:-1] #Remove Newline
        rpsList.append(column.split(" "))
    
    print(rpsList)

    solution1 = solutionPart1(rpsList)
    print("The total score if everything goes exactly to plan is: "+str(solution1))

    solution2 = solutionPart2(rpsList)
    print("The total score if everything goes exactly to the strategy guide is: "+str(solution2))
