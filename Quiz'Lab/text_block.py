import pygame
from game_object import GameObject
from colors import Color


class TextBlock(GameObject):

    def __init__(self, x, y, w, h, text, question=False):
        super().__init__(x, y, w, h)
        self.text = text
        self.x_padding = x + 10
        self.y_padding = y + 13
        self.font = pygame.font.Font("upheavtt.ttf", 30)
        self.DEFAULT_BACK_COLOR = (94,94,94)
        self.back_color = self.DEFAULT_BACK_COLOR
        self.border = pygame.Rect(x-5, y-5, w+10, h+10)
        self.borderColor = (28,28,28)
        self.is_question = question
        self.pos = (x,y)
        self.size = (w,h)

    def draw(self, surface):
        pygame.draw.rect(surface, self.borderColor, self.border)
        pygame.draw.rect(surface, self.back_color, self.bounds)
        if self.is_question:
            surface.blit(self.font.render(self.text, False, (0, 0, 0)), (self.pos[0] + (self.size[0] // 2) - (pygame.font.Font.size(self.font, self.text)[0] // 2), self.pos[1] + (self.size[1] // 2) - (pygame.font.Font.size(self.font, self.text)[1] // 2)))
        else:
            surface.blit(self.font.render(self.text, False, (0, 0, 0)),
                         (self.x_padding, self.y_padding))

    def update(self):
        pass
