import pygame

class Status(object):

    def __init__(self, size=(400, 200), pos=(0, 0)):
        self.pos = pos
        self.size = size
        self.charge = 3
        self.battery = pygame.image.load("img/battery.png").convert_alpha()
        self.charge_bar = pygame.image.load("img/charge.png").convert_alpha()

    def setCharge(self, charge):
            self.charge = charge
            if charge > 11:
                self.charge = 11
            if charge < 0:
                self.charge = 0

    def getCharge(self):
        return self.charge

    def drawBattery(self, screen):
        screen.blit(self.battery, (self.pos[0], self.pos[1]))
        posBar = 30
        self.charge_bar = self.charge_bar.convert_alpha()
        if self.charge < 5:
            fill(self.charge_bar, pygame.Color(255, 0, 0))
        elif self.charge < 9 and self.charge > 4:
            fill(self.charge_bar, pygame.Color(255, 220, 0))
        else:
            fill(self.charge_bar, pygame.Color(0, 255, 0))

        for i in range(self.charge):
            screen.blit(self.charge_bar, (self.pos[0] + posBar, self.pos[1]+30))
            posBar += 30


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

    def setSize(self, size=(400, 200)):
        self.size = size


def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))
