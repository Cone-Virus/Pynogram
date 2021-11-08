import pygame
import get_path

class Timer():
    timerRunning = True # counts up when true, stops when False
    refTime = 0 # time when timer started
    currTime = 0 # time relative to when timer started; what to display on the screen
    timerText = "" # text to show timer on screen

    # Used to display the time on screen
    numSeconds = 0
    numMinutes = 0

    def __init__(self):
        self.timerRunning = True
        self.refTime = pygame.time.get_ticks()
        self.currTime = pygame.time.get_ticks() - self.refTime # get the relative time
        self.numSeconds = 0
        self.numMinutes = 0
        self.timerText = ""

    def isRunning(self): # true if timer running, false otherwise (getter)
        return self.timerRunning

    def setRunning(self, status): # set timerRunning to status (setter)
        self.timerRunning = status

    def resetTimer(self): # start counting from 0
        self.refTime = pygame.time.get_ticks() # updates the reference time (new starting point)

    def displayTime(self, surface, themeMgr): # display the time on the screen
        # Only update time if timer is running
        if self.timerRunning:
            # Determine amount of time passed since refTime was set up
            self.currTime = pygame.time.get_ticks() - self.refTime
        self.numSeconds = self.currTime // 1000 # ms -> s
        self.numMinutes = self.numSeconds // 60 # s -> min
        self.numSeconds = self.numSeconds - (self.numMinutes * 60) # remove the time accounted for in numMinutes

        # Border around timer
        pygame.draw.rect(surface, themeMgr.getFontColor(), pygame.Rect(745, 45, 110, 55))
        # Background for timer
        pygame.draw.rect(surface, themeMgr.getBgColor(), pygame.Rect(750, 50, 100, 45))

        # Display timer text (minutes and seconds)
        self.timerText = "{0:02}:{1:02}".format(self.numMinutes, self.numSeconds)
        font = pygame.font.Font(get_path.get_path("assets/font/freesansbold.ttf"), 30)
        text = font.render(self.timerText, True, themeMgr.getFontColor())
        surface.blit(text, [760, 60])
