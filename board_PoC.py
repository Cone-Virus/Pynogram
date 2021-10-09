import pygame
import math

# Initial Board
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
board0x = [[0],
        [1,1],
        [1,1],
        [0],
        [1,1],
        [1,1],
        [4],
        [0],
        [0],
        [0]
        ]
board0y = [[0],
        [1],
        [1],
        [2,1],
        [1],
        [1],
        [2,1],
        [1],
        [1],
        [0]
        ]

class gameboard():
    def __init__(self,size,board):
        self.color = (255,255,255)
        self.board = []
        if board == 0 and size == 10:
            self.Sboard = board0
            self.SX = board0x
            self.SY = board0y
            self.load_board()
        if size == 5:
            self.boardsize = 180
        elif size == 10:
            self.boardsize = 355
        elif size == 15:
            self.boardsize = 530
        self.size = size
        pygame.draw.rect(surface, (0,0,0), pygame.Rect(200, 250, self.boardsize, self.boardsize))
        for x in range(self.size):
            test = []
            for y in range(self.size):
                self.button(x,y)
                test.append(0)
            self.board.append(test)
        pygame.display.flip()

    def button(self,x,y):
        pygame.draw.rect(surface, self.color, pygame.Rect(205 + (x * 35), 255 + (y * 35), 30, 30))

    def clear_board(self):
        for x in range(self.size):
            for y in range(self.size):
                self.button(x,y)
                self.board[x][y] = 0
        pygame.display.update()

    def load_board(self):
        posX = 0 # Left Side
        for x in self.SX:
            count = 0 # For numbers side to side
            for y in x:
                font = pygame.font.Font('freesansbold.ttf', 30)
                text = font.render(str(y), True, (0,0,0))
                surface.blit(text,(175 - (count * 35) ,255 + (posX * 35)))
                count = count + 1
            posX = posX + 1 
        posX = 0 # Top Side
        for x in self.SY:
            count = 0 # For numbers top to bottom
            x = reversed(x)
            for y in x:
                font = pygame.font.Font('freesansbold.ttf', 30)
                text = font.render(str(y), True, (0,0,0))
                surface.blit(text,(210 + (posX * 35),(220  - (count * 35))))
                count = count + 1
            posX = posX + 1


        


    def convert_space(self,x,y): # Function responsible for converting X,Y mouse coordinates into array numbers
        new_x = math.floor((x - 205) / 35)
        new_y = math.floor((y - 255) / 35)
        if new_x < 0:
            new_x = 0
        if new_y < 0:
            new_y = 0
        if new_x >= self.size:
            new_x = self.size - 1
        if new_y >= self.size:
            new_y = self.size - 1
        return new_x, new_y

    def fillspace(self,x,y,selection):
        if x <= self.boardsize + 205 and y <= self.boardsize + 255 and x >= 200 and y >= 250:
            space = self.convert_space(x,y)
            if selection == 1:
                if self.board[space[0]][space[1]] == 1:
                    pygame.draw.rect(surface, self.color, pygame.Rect(205 + (space[0] * 35), 255 + (space[1] * 35), 30, 30))
                    self.board[space[0]][space[1]] = 0
                else:
                    pygame.draw.rect(surface, (45,45,45), pygame.Rect(205 + (space[0] * 35), 255 + (space[1] * 35), 30, 30))
                    self.board[space[0]][space[1]] = 1
            elif selection == 3:
                if self.board[space[0]][space[1]] == -1:
                    pygame.draw.rect(surface, self.color, pygame.Rect(205 + (space[0] * 35), 255 + (space[1] * 35), 30, 30))
                    self.board[space[0]][space[1]] = 0
                else:
                    pygame.draw.rect(surface, (90,45,90), pygame.Rect(205 + (space[0] * 35), 255 + (space[1] * 35), 30, 30))
                    self.board[space[0]][space[1]] = -1
        pygame.display.update()




screen = pygame.init()
surface = pygame.display.set_mode((900,900))
surface.fill((255,255,255))


board = gameboard(10,0)
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1 or e.button == 3:
                x,y = pygame.mouse.get_pos()
                selection = e.button
                board.fillspace(x,y,selection)
