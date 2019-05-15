import pygame

class Bubble(object):
    def __init__(self, text, pos, size):
        self.text = text
        self.pos = pos
        self.size = size
        pygame.font.init()
        self.bubble = pygame.image.load("img/bubble.png")


    def draw(self, surface):

        surface.blit(pygame.transform.scale(self.bubble,self.size), (self.pos))
        self.render_text(surface)


    def update(self):
        pass


    def render_text(self, surface):
        font = pygame.font.Font("upheavtt.ttf", 40)
        if len(self.text) > 40:
            i = 40
            while self.text[i - 1] != " ":
                i -= 1
            surface.blit(font.render(self.text[:i].replace("\n", ""), 1, (0, 0, 0)), (self.pos[0]+50, self.pos[1]+150))
            surface.blit(font.render(self.text[i:].replace("\n", ""), 1, (0, 0, 0)), (self.pos[0]+50, self.pos[1]+175))
        else:
            surface.blit(font.render(self.text.replace("\n", ""), 1, (0, 0, 0)), (self.pos[0]+50, self.pos[1]+150))
