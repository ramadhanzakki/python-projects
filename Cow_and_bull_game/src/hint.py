import random

class Hint:
    def __init__(self, answer: list) -> str:
        self.answer = answer

    def hintAnswer(self):
        hint = (random.choice(self.answer))
        return str(hint)