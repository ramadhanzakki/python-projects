import random
from src.transform import Transform
from src.bullcheck import BullCheck
from src.cowcheck import CowCheck


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

    while True:
        # User input
        try:
            answer = int(input('Guess: '))
        except ValueError:
            print(f'WARNING⚠️: Guess is number only')
            continue
        
        # Transform answer to array
        rand_nums_arr = Transform(rand_nums)
        answer_arr = Transform(answer)

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
