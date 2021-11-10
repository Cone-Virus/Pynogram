import pygame

# Slow blinking animation to show solution and then clear board
# Returns blinkSoln = false when finished last step of animation, true otherwise
def blink_anim(timer, board, surface, themeMgr, startTime):
    currTime = pygame.time.get_ticks()
    if (currTime - startTime) >= 5000: # last step - hide solution
        board.clearGrid()
        timer.resetTimer()
        timer.setRunning(True)
        return False # done with animation
    elif (currTime - startTime) >= 4000: # show solution again
        board.showSolution()
        board.displayBoxes(surface, themeMgr)
        pygame.display.update()
    elif (currTime - startTime) >= 3000: # hide solution
        board.clearGrid()
        board.displayBoxes(surface, themeMgr)
        pygame.display.update()
    else: # show solution
        timer.resetTimer()
        timer.displayTime(surface, themeMgr) # show timer
        timer.setRunning(False)
        pygame.display.update()
    return True # not done with animation
