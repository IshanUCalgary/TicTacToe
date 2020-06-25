import tictactoe_draw
import tictactoe_logic
import stddraw

turn = 0
tictactoe_draw.setScales()
while True:
    if not tictactoe_logic.checkIfWon() and turn < 9:
        tictactoe_draw.drawCanvas()
        if stddraw.mousePressed():
            posX = stddraw.mouseX()
            posY = stddraw.mouseY()
            quadrant = tictactoe_logic.checkQuadrant(posX,posY)
            if tictactoe_logic.checkIfQuadrantFilled(quadrant):
                turn += 1
                tictactoe_draw.turnStatement(turn)
            if turn % 2 == 0 and tictactoe_logic.checkIfQuadrantFilled(quadrant):
                tictactoe_draw.drawO(tictactoe_logic.centerX,tictactoe_logic.centerY)
                tictactoe_logic.fillQuadrant(quadrant,'O')
            elif tictactoe_logic.checkIfQuadrantFilled(quadrant):
                tictactoe_draw.drawX(tictactoe_logic.centerX,tictactoe_logic.centerY)
                tictactoe_logic.fillQuadrant(quadrant,'X')

    elif turn >= 9:
        tictactoe_draw.win(tictactoe_logic.winner,turn)
    else:
        tictactoe_draw.win(tictactoe_logic.winner,turn)
    tictactoe_draw.show(10)
