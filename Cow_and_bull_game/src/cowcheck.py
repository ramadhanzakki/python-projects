class CowCheck:
    def __init__(self, inputNumber: list, correct: list) -> int:
        self.input = inputNumber
        self.correct = correct

    def checkCowNumber(self):
        count = 0

        for i in self.correct:
            if i in self.input:
                count += 1

        return count
