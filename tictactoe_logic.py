import math

centerX = 0
centerY = 0
winner = ''
matrix = ['0','1','2','3','4','5','6','7','8']

def checkWhoWins(countX,countO):
    global winner
    if countX == 3:
        winner = 'X'
        return True
    if countO == 3:
        winner = 'O'
        return True
    return False


def checkQuadrant(posX,posY):
    global centerX, centerY
    quadrant = 0
    if posX > -10.0 and posX < -3.33 and posY > 3.33 and posY < 10.0:
        quadrant = 0
        centerX = (-10.0+-3.33) / 2
        centerY = (10.0 + 3.33) / 2
    if posX > -3.33 and posX < 3.33 and posY > 3.33 and posY < 10.0:
        quadrant = 1
        centerX = 0.0
        centerY = (10.0 + 3.33) / 2
    if posX > 3.33 and posX < 10.0 and posY > 3.33 and posY < 10.0:
        quadrant = 2
        centerX = (10.0 + 3.33) / 2
        centerY = (10.0 + 3.33) / 2
    if posX > -10.0 and posX < -3.33 and posY > -3.33 and posY < 3.33:
        quadrant = 3
        centerX = (-10.0+-3.33) / 2
        centerY = 0.0
    if posX > -3.33 and posX < 3.33 and posY > -3.33 and posY < 3.33:
        quadrant = 4
        centerX = 0.0
        centerY = 0.0
    if posX > 3.33 and posX < 10.0 and posY > -3.33 and posY < 3.33:
        quadrant = 5
        centerX = (10.0 + 3.33) / 2
        centerY = 0.0
    if posX > -10.0 and posX < -3.33 and posY > -10.0 and posY < -3.33:
        quadrant = 6
        centerX = (-10.0+-3.33) / 2
        centerY = (-10.0 + -3.33) / 2
    if posX > -3.33 and posX < 3.33 and posY > -10.0 and posY < -3.33:
        quadrant = 7
        centerX = 0.0
        centerY = (-10.0 + -3.33) / 2
    if posX > 3.33 and posX < 10.0 and posY > -10.0 and posY < -3.33:
        quadrant = 8
        centerX = (10.0 + 3.33) / 2
        centerY = (-10.0 + -3.33) / 2

    return quadrant

def fillQuadrant(quadrant,symbol):
    if checkIfQuadrantFilled(quadrant):
        matrix[quadrant] = symbol

def checkIfQuadrantFilled(quadrant):
    if matrix[quadrant] != 'X' and matrix[quadrant] != 'O':
        return True
    else:
        return False

def checkHorizontal():
    countX = 0
    countO = 0
    start = 0
    stop = 3
    while stop <= 9:
        for everyRow in range(start,stop):
            if matrix[everyRow] == 'X':
                countX += 1
            elif matrix[everyRow] == 'O':
                countO += 1
        if checkWhoWins(countX,countO):
            return True
            break
        else:
            countX = 0
            countO = 0
            start += 3
            stop += 3
    return False

def checkVertical():
    global winner
    countX = 0
    countO = 0
    start = 0
    stop = 7
    while stop <= 9:
        for everyRow in range(start,stop,3):
            if matrix[everyRow] == 'X':
                countX += 1
            elif matrix[everyRow] == 'O':
                countO += 1
        if checkWhoWins(countX,countO):
            return True
            break
        else:
            countX = 0
            countO = 0
            start += 1
            stop += 1
    return False

def checkDiagonal():
    countX = 0
    countO = 0
    start = 2
    increment = 2
    stop = 7
    for i in range(2):
        for everyRow in range(start,stop,increment):
            if matrix[everyRow] == 'X':
                countX += 1
            elif matrix[everyRow] == 'O':
                countO += 1
        if checkWhoWins(countX,countO):
            return True
            break
        else:
            countX = 0
            countO = 0
            start = 0
            stop = 9
            increment = 4
    return False


def checkIfWon():
    if checkDiagonal() or checkVertical() or checkHorizontal():
        return True
    else:
        return False
