from button import Button
from colors import Color


class AnswerButton(Button):

    def __init__(self, x, y, w, h, text, on_click_func=None, is_it_correct_answer=False, question=False):
        super().__init__(x, y, w, h, text, on_click_func, question)
        self.is_it_correct_answer = is_it_correct_answer
        if self.is_it_correct_answer is True:
            self.PRESSED_BACK_COLOR = Color.WHITE
        else:
            self.PRESSED_BACK_COLOR = Color.WHITE

    def checkUserAnswer(self):
        return self.is_it_correct_answer
