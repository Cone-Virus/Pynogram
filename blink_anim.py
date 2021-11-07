import pygame

# Slow blinking animation to show solution and then clear board
def blink_anim(timer, board, surface):
    timer.resetTimer()
    timer.displayTime(surface) # show timer
    timer.setRunning(False)
    pygame.display.update()

    pygame.time.wait(3000)
    board.clearGrid()
    board.displayBoxes(surface)
    pygame.display.update()

    pygame.time.wait(1000)
    board.showSolution()
    board.displayBoxes(surface)
    pygame.display.update()

    pygame.time.wait(1000)
    board.clearGrid()
    timer.resetTimer()
    timer.setRunning(True)
    blinkSoln = False
