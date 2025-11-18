import random
from src.transform import Tools
from src.bullcheck import BullCheck
from src.cowcheck import CowCheck
from src.hint import Hint


def main():
    #header
    print('\n=================================')
    print('      🎉Cow and Bull Game🎉')
    print('=================================\n')

    while True:
        print('--- 🎚️Choice your difficulty ---')
        print('1. Easy')
        print('2. Medium')
        print('3. Hard')

        try:
            difficulty_choice = int(input('Your choice: '))
            break
        except ValueError:
            print('WARNING⚠️: Select 1/2/3!')
            continue

    # Creating the random number
    if difficulty_choice == 1:
        rand_nums = random.randrange(1000, 9999, 1)
        target_length = 4
    elif difficulty_choice == 2:
        rand_nums = random.randrange(10000, 99999, 1)
        target_length = 5
    elif difficulty_choice == 3:
        rand_nums = random.randrange(100000, 999999, 1)
        target_length = 6

    count = 0
    rand_nums_arr = Tools(rand_nums)

    while True:
        count += 1

        if count % 3 == 0:
            rand_hint = Hint(rand_nums_arr.changeToArray())
            print(f'💡Hint: One of the numbers is {rand_hint.hintAnswer()}')

        # User input
        try:
            answer = int(input(f'Guess {target_length}-digit number: '))
        except ValueError:
            print(f'WARNING⚠️: Guess is number only')
            continue
        
        # Tools answer to array
        answer_arr = Tools(answer)

        # Check
        cow = CowCheck(answer_arr.changeToArray(), rand_nums_arr.changeToArray())
        bull = BullCheck(answer_arr.changeToArray(), rand_nums_arr.changeToArray())

        total_correct_digits = cow.checkCowNumber()
        bull_count = bull.check()

        cow_count = total_correct_digits - bull_count

        print(f'{cow_count} Cows, {bull_count} Bulls')

        if bull_count == target_length:
            print(f'\n--- 🎉CONGRATULATION, You Guess the number ---')
            break

        


if __name__ == "__main__":
    main()
