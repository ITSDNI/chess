import pygame
import sys
pygame.init()
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w - 200
SCREEN_HEIGHT = infoObject.current_h - 200
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Two-Player Pygame Chess!')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
objects = []


class Button():
    def __init__(self, x, y, width, height, buttonText='Button',color = '#ffffff', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.pressed = False
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction

        self.fillColors = {
            'normal': color,
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)
        
    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                self.pressed = True
                self.onclickFunction()
            # elif self.pressed:
            #     self.pressed = False
            #     self.buttonSurface.fill(self.fillColors['normal'])
        
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

class ChampionDashboard():
    def __init__(self,x,y,name,avatar):
        self.name = name
        self.avatar = avatar
        self.score = 0
        pygame.draw.circle(screen,'green',[0,0],50)