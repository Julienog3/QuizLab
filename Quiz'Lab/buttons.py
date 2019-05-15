import pygame


class Button(object):

    def __init__(self, text, size=(300, 100), pos=(0, 0), backgroundColor=(255, 255, 255), borderColor=(0, 0, 0),
                 textColor=(64, 64, 64), hilightColor=(0, 0, 50, 80), clickState=False):
        self.pos = pos
        self.size = size
        self.text = text
        self.backgroundColor = backgroundColor
        self.textColor = textColor
        self.borderColor = borderColor
        self.hilightColor = hilightColor
        self.clickState = clickState

    def __repr__(self):
        return self.getText()

    def getText(self):
        return self.text

    def getPos(self):
        return self.pos

    def setSize(self, size=(100, 50)):
        self.size = size

    def setPos(self, pos_x, pos_y):
        screen_width, screen_height = pygame.display.get_surface().get_size()
        if pos_x == "middle":
            x = (screen_width // 2 - self.size[0] // 2)
        else:
            x = pos_x
        if pos_y == "middle":
            y = (screen_height // 2 - self.size[1] // 2)
        else:
            y = pos_y
        self.pos = (x, y)

    def setHilightColor(self, color):
        self.hilightColor = color

    def setText(self, text):
        self.text = text

    def setBackgroundColor(self, color=(0, 0, 0)):
        self.backgroundColor = color

    def setTextColor(self, color=(255, 255, 255)):
        self.textColor = color

    def setBorderColor(self, color):
        self.borderColor = color

    def drawButton(self, screen):
        pygame.draw.rect(screen, self.borderColor, (self.pos[0], self.pos[1], self.size[0], self.size[1]))
        pygame.draw.rect(screen, self.backgroundColor,
                         (self.pos[0] + 3, self.pos[1] + 3, self.size[0] - 6, self.size[1] - 6))
        font = pygame.font.Font("upheavtt.ttf", 50)
        textButton = font.render(self.text, 40, self.textColor)
        screen.blit(textButton, (self.pos[0] + (self.size[0] // 2) - (pygame.font.Font.size(font, self.text)[0] // 2),
                                 self.pos[1] + (self.size[1] // 2) - (pygame.font.Font.size(font, self.text)[1] // 2)))
        if self.isHovered():
            self.hilight(screen)

    def isClicked(self):
        if pygame.mouse.get_pressed()[0] == 1 and self.isHovered():
            self.clickState = True
        elif self.clickState:
            self.clickState = False
            return True
        else:
            return False

    def isHovered(self):
        if pygame.mouse.get_pos()[0] > self.pos[0] and pygame.mouse.get_pos()[1] > self.pos[1] and \
                pygame.mouse.get_pos()[0] < self.pos[0] + self.size[0] and pygame.mouse.get_pos()[1] < self.pos[1] + \
                self.size[1]:
            return True
        else:
            return False

    def hilight(self, screen):
        s = pygame.Surface((self.size[0], self.size[1]), pygame.SRCALPHA)  # per-pixel alpha
        s.fill(self.hilightColor)  # notice the alpha value in the color
        screen.blit(s, (self.pos[0], self.pos[1]))
