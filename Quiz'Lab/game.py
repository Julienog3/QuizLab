import pygame
import sys
import robot 
from bubble import Bubble
import status
import buttons
from text_block import TextBlock
from answer_button import AnswerButton
from question_object import Question_Object

class GameState:#classe comportantles 3 états du jeu
    menu, game, game_over = range(3)


class Game:#classe comportant toutes les definitions utilisés dans le jeu

    def __init__(self):#definition initialisant chaque élément utilisé dans le code
        pygame.init()
        pygame.font.init()
        self.question_height = 150
        self.answer_height = 150
        self.surface = pygame.display.set_mode((1920, 1080),pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load("img/bg.png").convert()
        self.fg = pygame.image.load("img/plan1.png").convert_alpha()
        self.mouse_handlers = []
        self.objects = []
        self.answer_objects = []
        self.current_question = None
        self.current_question_i = -1
        self.status = status.Status((400,200), (1400,80))
        self.robot = robot.Robot("myRobot")
        self.robot_size = self.robot.setSize(800,800)
        self.robot_pos = self.robot.setPos(1150,300)
        self.wrong_sound = pygame.mixer.Sound("wrong.wav")
        self.true_sound = pygame.mixer.Sound("true.wav")
        self.gameover_sound = pygame.mixer.Sound("gameover.wav")
        self.retry_button = buttons.Button("Recommencer", size=(400, 200), pos = (600, 700), borderColor=(64,64,64), backgroundColor=(204, 204, 204),hilightColor=(41, 41, 41, 80),textColor=(0,0,0))
        self.state = GameState.game
        self.questions = [Question_Object('Combien font 56+69944?', ('70036', ' 70101', '70000', '69999'), 2),
                          Question_Object('The Hundred Years War was fought between what two countries?',
                                          ('Italy and Carthage', 'England and Germany', 'France and England', 'Spain and France'), 2),
                          Question_Object('Who fought in the war of 1812?', ('Andrew Jackson', 'Arthur Wellsley', 'Otto von Bismarck', 'Napoleon'), 0),
                          Question_Object('American involvement in the Korean War took place in which decade?', ('1950s', '1960s', '1970s', '1980s'), 0),
                          Question_Object('The Battle of Hastings in 1066 was fought in which country?  ', ('France', 'Russia', 'England', 'Norway'), 3),
                          Question_Object('The Magna Carta was published by the King of which country? ', ('France', 'Austria', 'Italy', 'England'), 3),
                          Question_Object('The first successful printing press was developed by this man.', ('Johannes Gutenburg', 'Benjamin Franklin', 'Sir Isaac Newton', 'Martin Luther'), 0)

                          ]
        self.nextQuestion()
        self.game_over_text_block = TextBlock(1920/2, 1080/2, 500, 50, "Game over")

    def update(self):#definition mettant à jour l'écran
        for item in self.objects:
            item.update()

        for item in self.answer_objects:
            item.update()

    def draw(self):#definition plaçant les éléments sur l'écran
        for item in self.objects:
            item.draw(self.surface)

        for item in self.answer_objects:
            item.draw(self.surface)

        if self.state == GameState.game_over:
            self.retry_button.drawButton(self.surface)
            self.robot.setEmote()

    def handleEvents(self):#definition prenant en charge les évenements dû à l'action de l'utilisateur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type in (pygame.MOUSEBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def addTextBlock(self, x, y, w, h, text):#definition ajoutant des blocs de texte
        self.objects.append(TextBlock(x, y, w, h, text))

    def addAnswerButton(self, x, y, w, h, text, onclick_func, is_it_correct):#definition ajoutant des boutons
        button1 = AnswerButton(x, y, w, h, text, onclick_func, is_it_correct, question=True)
        self.answer_objects.append(button1)
        self.mouse_handlers.append(button1.handleMouseEvent)

    def checkAnswer(self, obj):#definition verifiant si la reponse est bonne
        if obj.is_it_correct_answer is True:
            self.status.setCharge(self.status.getCharge() + 1)
            self.robot.setHumor(1)
            self.robot.setEmote()
            self.true_sound.play()
        else:
            self.status.setCharge(self.status.getCharge() - 1)
            self.robot.setHumor(-1)
            self.robot.setEmote()
            self.wrong_sound.play()

        if self.status.getCharge() == 0:
            self.gameOver()

        if self.status.getCharge() == 11:
            self.gameOver()

        if self.state != GameState.game_over:
            self.nextQuestion()

    def gameOver(self): #definition de l'écran de fin du quiz lorsque celui-ci est terminé
        self.state = GameState.game_over
        self.cleanScreen()
        if self.status.getCharge() == 11:
            self.game_over_text_block = TextBlock(1920/2-500, 1080/2, 470, 50, "Bravo, la fusée a décollée !")
            self.robot.setHumor(1)
        else:
            self.game_over_text_block = TextBlock(1920/2-500, 1080/2, 600, 50, "Oh mince, la fusée n'a pas décollée !")
            self.gameover_sound.play()
            self.robot.setHumor(-1)





        self.objects.append(self.game_over_text_block)




    def cleanScreen(self): #définition enlevant tout les éléments de l'écran
        del self.answer_objects[:]
        del self.objects[:]
        del self.mouse_handlers[:]

    def nextQuestion(self): #definition appliqué à chaque nouvelle question

        del self.answer_objects[:]
        del self.mouse_handlers[:]
        self.current_question_i += 1
        if self.current_question_i >= len(self.questions):
            self.gameOver()
        else:
            self.current_question = self.questions[self.current_question_i]
            self.surface.blit(self.bg, (0, 0))
            self.surface.blit(self.fg, (0, 0))
            self.objects.append(Bubble(self.current_question.question_text, (200,650), (1000,400)))

            answers = self.current_question.answers

            i = 0
            x = 300
            y = 300
            y2 = y + 165

            for item in answers:
                if self.current_question.correct_answer == i:
                    is_it_correct = True
                else:
                    is_it_correct = False

                self.addAnswerButton(x, y,
                                     400, self.answer_height, item, self.checkAnswer, is_it_correct)
                if i % 2 == 0:
                    x += 415
                else:
                    x -= 415

                if i == 1:
                    y = y2

                i += 1

            self.answer_height = 150


    def run(self): #définition du lancement du Quiz
        while True:
            self.surface.blit(self.bg, (0,0))
            self.draw()
            self.robot.drawRobot(self.surface)
            self.surface.blit(self.fg, (0,0))
            self.update()
            self.status.drawBattery(self.surface)
            self.handleEvents()
            if self.retry_button.isClicked() and self.state == GameState.game_over:
                Game().run()
            pygame.display.update()
            self.clock.tick(60)


Game1 = Game()


Game1.run()


