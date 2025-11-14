import random
from src.transform import Transform
from src.bullcheck import BullCheck
from src.cowcheck import CowCheck


def main():
    #header
    print('\n=================================')
    print('      🎉Cow and Bull Game🎉')
    print('=================================\n')


    # Creating the random number
    rand_nums = random.randrange(1000, 9999, 1)

    while True:
        # User input
        try:
            answer = int(input('Guess: '))
        except ValueError:
            print(f'WARNING⚠️: Guess is number only')
            continue
        
        # Transform answer to array
        answer_arr = Transform(answer)
        rand_nums_arr = Transform(rand_nums)

        # Check
        cow = CowCheck(answer_arr.changeToArray(), rand_nums_arr.changeToArray())
        bull = BullCheck(answer_arr.changeToArray(), rand_nums_arr.changeToArray())

        total_correct_digits = cow.checkCowNumber()
        bull_count = bull.check()

        cow_count = total_correct_digits - bull_count

        print(f'{cow_count} Cows, {bull_count} Bulls')

        if bull_count == 4:
            print(f'\n--- 🎉CONGRATULATION, You Guess the number ---')
            break

        


if __name__ == "__main__":
    main()
