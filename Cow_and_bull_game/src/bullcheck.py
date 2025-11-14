class BullCheck:
    def __init__(self, inputNum: list, correct: list) -> int:
        self.input = inputNum
        self.correct = correct

    def check(self):
        count = 0

        for i, num in enumerate(self.correct):
            if self.input[i] == num:
                count += 1

        return count