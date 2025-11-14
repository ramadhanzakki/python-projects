class Transform:
    def __init__(self, inputNum):
        self.input = inputNum

    def changeToArray(self):
        array = []

        for num in str(self.input):
            array.append(int(num))

        return array
