import pygame
import time
import math


board0 = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,1,0,0,0],
        [0,0,0,1,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0,1,0],
        [0,0,1,0,0,0,0,1,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
        ]

class gameboard():
    def __init__(self,size):
        self.color = (255,255,255)
        self.board = []
        pygame.draw.rect(surface, (0,0,0), pygame.Rect(150, 150, 555, 555))
        for x in range(10):
            test = []
            for y in range(10):
                self.button(x,y)
                test.append(0)
            self.board.append(test)
        pygame.display.update()

    def button(self,x,y):
        pygame.draw.rect(surface, self.color, pygame.Rect(155 + (x * 55), 155 + (y * 55), 50, 50))

    def clear_board(self):
        for x in range(10):
            for y in range(10):
                self.button(x,y)
                self.board[x][y] = 0
        pygame.display.update()

    def convert_space(self,x,y): # Function responsible for converting X,Y mouse coordinates into array numbers
        new_x = math.floor((x - 155) / 55)
        new_y = math.floor((y - 155) / 55)
        if new_x < 0:
            new_x = 0
        if new_y < 0:
            new_y = 0
        return new_x, new_y

    def fillspace(self,x,y,selection):
        if x <= 700 and y <= 700 and x >= 150 and y >= 150:
            space = self.convert_space(x,y)
            if selection == 1:
                if self.board[space[0]][space[1]] == 1:
                    pygame.draw.rect(surface, self.color, pygame.Rect(155 + (space[0] * 55), 155 + (space[1] * 55), 50, 50))
                    self.board[space[0]][space[1]] = 0
                else:
                    pygame.draw.rect(surface, (45,45,45), pygame.Rect(155 + (space[0] * 55), 155 + (space[1] * 55), 50, 50))
                    self.board[space[0]][space[1]] = 1
            elif selection == 3:
                if self.board[space[0]][space[1]] == -1:
                    pygame.draw.rect(surface, self.color, pygame.Rect(155 + (space[0] * 55), 155 + (space[1] * 55), 50, 50))
                    self.board[space[0]][space[1]] = 0
                else:
                    pygame.draw.rect(surface, (90,45,90), pygame.Rect(155 + (space[0] * 55), 155 + (space[1] * 55), 50, 50))
                    self.board[space[0]][space[1]] = -1
        pygame.display.update()




screen = pygame.init()
surface = pygame.display.set_mode((800,800))
surface.fill((255,255,255))


board = gameboard(2)
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1 or e.button == 3:
                x,y = pygame.mouse.get_pos()
                selection = e.button
                board.fillspace(x,y,selection)
