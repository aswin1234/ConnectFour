#inputHi = input("Please Enter a Number:")
#print(inputHi)
twoDimensionalArray = []
oneDimensionalArray = ['*', '*', '*', '*', '*', '*', '*']

for i in range(7):
    oneDimensionalArray = ['*', '*', '*', '*', '*', '*', '*']
    twoDimensionalArray.append(oneDimensionalArray)
twoDimensionalArray.append(['0', '1', '2', '3', '4', '5', '6'])

def printBoard(twoDimensionalArray):
    eachLine = ""
    for elements in twoDimensionalArray:
        for stuff in elements:
            eachLine = eachLine + stuff + " "
        print(eachLine)
        eachLine = ""

gamesGoingOn = True


def move( integer, player):
    i = 6
    while (i != 0):
        if (twoDimensionalArray[i][integer] == '*'):   
            twoDimensionalArray[i][integer] = player
            return
        i = i - 1
    print("Illegal Move")


#lastMove is an integer detailing the last move
"""
def isWinner(lastMove, player):
    isVerticle(1, True) or isHorizontal(lastMove, player)
"""
def isHorizontal(lastMove, player):
    counter = 0
    verticalPosition = 7
    while verticalPosition >= 0:
        if (twoDimensionalArray[verticalPosition][lastMove] == player):
            break
        else:
            verticalPosition -= 1   
    i = 0
    while i < 7:
        if (twoDimensionalArray[verticalPosition][i] == player):
            counter = counter + 1
            if (counter == 4):
                return True
        else:
            counter = 0
            i += 1
        print(counter)
    return False

def isVerticle(lastMove, player):
    i = 6
    counter = 0
    while i != 0:
        if (twoDimensionalArray[i][lastMove] == player):
            counter = counter + 1
            print(player)
            print(twoDimensionalArray[i][lastMove])
            if (counter == 4):
                return True
        else:
            counter = 0
            i -= 1
    return True            

printBoard(twoDimensionalArray)
print(isVerticle(1, "o"))
move(1, "x")
move(2, "x")
move(1, "x")
move(1, "x")
move(1, "x")
print(isVerticle(1, "o"))
printBoard(twoDimensionalArray)




