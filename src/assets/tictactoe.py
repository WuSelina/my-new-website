# Selina Wu
# Anything user needs to know:
    # Legal values for graphical inputs are 100 to 1000 inclusive
    # In that case that player 1 or 2 wins, program will give the winner and close the game window, but gives an error that can be ignored.
# Extra credit work:
    # Resolved when there is a tie.

from graphics import *

n = int(input("Window side length in pixels:"))
print()

def drawX(line1, line2, win):
    line1.setFill('red')
    line2.setFill('red')
    line1.draw(win)
    line2.draw(win)
def drawO(cir, win):
    cir.setOutline('blue')
    cir.draw(win)

def winning(board, win):
    if (board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1) or \
            (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1) or \
            (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1) or \
            (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1) or \
            (board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1) or \
            (board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1) or \
            (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1) or \
            (board[2][0] == 1 and board[1][1] == 1 and board[0][2] == 1):
        print("PLAYER 1 IS THE WINNER!! Click anywhere in the window to close.")
        win.getMouse()
        win.close()
    elif (board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2) or \
            (board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2) or \
            (board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2) or \
            (board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2) or \
            (board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2) or \
            (board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2) or \
            (board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2) or \
            (board[2][0] == 2 and board[1][1] == 2 and board[0][2] == 2):
        print("PLAYER 2 IS THE WINNER! Click anywhere in the window to close.")
        win.getMouse()
        win.close()

def main():
    win = GraphWin('Tic Tac Toe', n, n)
    vline1 = Line(Point(n / 3, 0), Point(n / 3, n))
    vline2 = Line(Point((2 * n) / 3, 0), Point((2 * n) / 3, n))
    hline1 = Line(Point(0, n / 3), Point(n, n / 3))
    hline2 = Line(Point(0, (2 * n) / 3), Point(n, (2 * n) / 3))

    vline1.draw(win)
    vline2.draw(win)
    hline1.draw(win)
    hline2.draw(win)

    # Matrix:
    size = 3
    board = [[0] * size for i in range(size)]

    # GamePlay
    turn = 1
    i = 0
    while i < 9:

        if turn%2!=0:
            print("Player 1: click a square.")
            p1 = win.getMouse()
            px = p1.getX()
            py = p1.getY()

            if 0 < px < (n / 3) and 0 < py < (n / 3):
                if board[0][0] == 0:
                    board[0][0] = 1
                    line1 = Line(Point(n / 3, 0), Point(0, n / 3))
                    line2 = Line(Point(0, 0), Point(n / 3, n / 3))
                    drawX(line1, line2, win)
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
                    turn = turn - 1
            elif (n / 3) < px < (2 * n) / 3 and 0 < py < (n / 3):
                if board[0][1] == 0:
                    board[0][1] = 1
                    line1 = Line(Point(2 * n / 3, 0), Point(n / 3, n / 3))
                    line2 = Line(Point(n / 3, 0), Point(2 * n / 3, n / 3))
                    drawX(line1, line2, win)
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
                    turn = turn - 1
            elif (2 * n) / 3 < px < n and 0 < py < (n / 3):
                if board[0][2] == 0:
                    board[0][2] = 1
                    line1 = Line(Point(n, 0), Point(2 * n / 3, n / 3))
                    line2 = Line(Point(2 * n / 3, 0), Point(n, n / 3))
                    drawX(line1, line2, win)
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
                    turn = turn - 1
            elif 0 < px < (n / 3) and (n / 3) < py < (2 * n) / 3:
                if board[1][0] == 0:
                    board[1][0] = 1
                    line1 = Line(Point(n / 3, n / 3), Point(0, 2 * n / 3))
                    line2 = Line(Point(n / 3, 2 * n / 3), Point(0, n / 3))
                    drawX(line1, line2, win)
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
                    turn = turn - 1
            elif (n / 3) < px < (2 * n) / 3 and (n / 3) < py < (2 * n) / 3:
                if board[1][1] == 0:
                    board[1][1] = 1
                    line1 = Line(Point(n / 3, n / 3), Point(2 * n / 3, 2 * n / 3))
                    line2 = Line(Point(2 * n / 3, n / 3), Point(n / 3, 2 * n / 3))
                    drawX(line1, line2, win)
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
                    turn = turn - 1
            elif (2 * n) / 3 < px < n and (n / 3) < py < (2 * n) / 3:
                if board[1][2] == 0:
                    board[1][2] = 1
                    line1 = Line(Point(2 * n / 3, n / 3), Point(n, 2 * n / 3))
                    line2 = Line(Point(n, n / 3), Point(2 * n / 3, 2 * n / 3))
                    drawX(line1, line2, win)
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
                    turn = turn - 1
            elif 0 < px < (n / 3) and (2 * n) / 3 < py < n:
                if board[2][0] == 0:
                    board[2][0] = 1
                    line1 = Line(Point(n / 3, 2 * n / 3), Point(0, n))
                    line2 = Line(Point(0, 2 * n / 3), Point(n / 3, n))
                    drawX(line1, line2, win)
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
                    turn = turn - 1
            elif (n / 3) < px < (2 * n) / 3 and (2 * n) / 3 < py < n:
                if board[2][1] == 0:
                    board[2][1] = 1
                    line1 = Line(Point(n / 3, 2 * n / 3), Point(2 * n / 3, n))
                    line2 = Line(Point(n / 3, n), Point(2 * n / 3, 2 * n / 3))
                    drawX(line1, line2, win)
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
                    turn = turn - 1
            elif (2 * n) / 3 < px < n and (2 * n) / 3 < py < n:
                if board[2][2] == 0:
                    board[2][2] = 1
                    line1 = Line(Point(2 * n / 3, 2 * n / 3), Point(n, n))
                    line2 = Line(Point(n, 2 * n / 3), Point(2 * n / 3, n))
                    drawX(line1, line2, win)
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
                    turn = turn - 1

            winning(board, win)
            turn = turn + 1
            print()

        elif turn%2==0:
            print("Player 2: click a square.")
            p1 = win.getMouse()
            px = p1.getX()
            py = p1.getY()

            if 0 < px < (n / 3) and 0 < py < (n / 3):
                if board[0][0] == 0:
                    board[0][0] = 2
                    cir = Circle(Point(n / 6, n / 6), (n - 6) / 6)
                    drawO(cir, win)
                    turn = turn - 1
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
            elif (n / 3) < px < (2 * n) / 3 and 0 < py < (n / 3):
                if board[0][1] == 0:
                    board[0][1] = 2
                    cir = Circle(Point(n / 2, n / 6), (n - 6) / 6)
                    drawO(cir, win)
                    turn = turn - 1
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
            elif (2 * n) / 3 < px < n and 0 < py < (n / 3):
                if board[0][2] == 0:
                    board[0][2] = 2
                    cir = Circle(Point(2.5 * n / 3, n / 6), (n - 6) / 6)
                    drawO(cir, win)
                    turn = turn - 1
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
            elif 0 < px < (n / 3) and (n / 3) < py < (2 * n) / 3:
                if board[1][0] == 0:
                    board[1][0] = 2
                    cir = Circle(Point(n / 6, n / 2), (n - 6) / 6)
                    drawO(cir, win)
                    turn = turn - 1
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
            elif (n / 3) < px < (2 * n) / 3 and (n / 3) < py < (2 * n) / 3:
                if board[1][1] == 0:
                    board[1][1] = 2
                    cir = Circle(Point(n / 2, n / 2), (n - 6) / 6)
                    drawO(cir, win)
                    turn = turn - 1
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
            elif (2 * n) / 3 < px < n and (n / 3) < py < (2 * n) / 3:
                if board[1][2] == 0:
                    board[1][2] = 2
                    cir = Circle(Point(2.5 * n / 3, n / 2), (n - 6) / 6)
                    drawO(cir, win)
                    turn = turn - 1
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
            elif 0 < px < (n / 3) and (2 * n) / 3 < py < n:
                if board[2][0] == 0:
                    board[2][0] = 2
                    cir = Circle(Point(n / 6, 2.5 * n / 3), (n - 6) / 6)
                    drawO(cir, win)
                    turn = turn - 1
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
            elif (n / 3) < px < (2 * n) / 3 and (2 * n) / 3 < py < n:
                if board[2][1] == 0:
                    board[2][1] = 2
                    cir = Circle(Point(n / 2, 2.5 * n / 3), (n - 6) / 6)
                    drawO(cir, win)
                    turn = turn - 1
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1
            elif (2 * n) / 3 < px < n and (2 * n) / 3 < py < n:
                if board[2][2] == 0:
                    board[2][2] = 2
                    cir = Circle(Point(2.5 * n / 3, 2.5 * n / 3), (n - 6) / 6)
                    drawO(cir, win)
                    turn = turn - 1
                else:
                    print("Error! This square has already been taken. Please try again.")
                    i = i - 1

            winning(board, win)
            print()

        i = i + 1

    print("The game is TIED. Click in the window to close.")
    win.getMouse()
    win.close()

main()
