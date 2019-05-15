import pygame


class Robot(object):


    dicImg = {"happy" : pygame.image.load("img/robothappy.png"), "normal" : pygame.image.load("img/robot.png"), "angry" : pygame.image.load("img/robotwrong.png")}

    def __init__(self, text, size=(300, 100), pos=(0, 0)):
        self.pos = pos
        self.size = size
        self.text = text
        self.float = True
        self.emote = False
        self.emoteCountdown = 0
        self.floatFrame = 0
        self.floatHeight = 20
        self.img = self.dicImg["normal"]


    def setHumor(self, humor):
        """
        description : permet de modifier l'image du robot avec une humeur
        humor : humeur du robot
        syntaxe : robot.setHumor(robot.HAPPY|robot.NORMAL|robot.ANGRY)
        """
        if humor == -1:
            self.img = self.dicImg["angry"]
        elif humor == 1:
            self.img = self.dicImg["happy"]
        else:
            self.img = self.dicImg["normal"]

    def drawRobot(self, surface):
        self.doFloat()
        self.emoteUpdate()
        surface.blit(pygame.transform.scale(self.img, self.size), (self.pos[0], self.pos[1]))

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

    def switchFloat(self):
        self.float = not self.float

    def setSize(self, x, y):
        self.size = (x,y)

    def setFloatHeight(self, height):
        self.floatHeight = height

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

    def setTextColor(self, color=(255, 255, 255)):
        self.textColor = color

    def getTextColor(self):
        return self.textColor

    def emoteUpdate(self):
        if self.emote:
            self.emoteCountdown = 60
            self.emote = False
        if self.emoteCountdown > 0:
            self.emoteCountdown -= 1
        else:
            self.img = self.dicImg["normal"]

    def setEmote(self):
        self.emote = True

    def doFloat(self):
        if self.float:
            self.floatFrame += 1
            if self.floatFrame >= (self.floatHeight*2-1):
                self.floatFrame = 0
            elif self.floatFrame < self.floatHeight:

                self.pos = (self.pos[0], self.pos[1] + 1)
            else:
                self.pos = (self.pos[0], self.pos[1] - 1)
