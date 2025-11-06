import random


class Dice:
    def __init__(self, many_roll):
        self.dice = many_roll


    def roll(self):
        user_roll = 0
        for i in range(self.dice):
            user_roll += 1
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f'({die1},{die2}) {user_roll} roll')

while True:
    input_user = input("Roll the Dice? (y/n): ").lower()
    if input_user == 'y':
        while True:
            try:
                ho_many_rolls = int(input('how many dice? '))
                break
            except ValueError:
                print('input just number')
        rolling = Dice(ho_many_rolls)
        rolling.roll()
    elif input_user == "n":
        print("Thanks for playing")
        break
    else:
        print("Invalid choice!")
