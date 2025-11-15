from data.input.inventory import INVENTORY
from src.function import SearchingAlgorithm
from src.visual import VisualInventory
import time
import sys


def main():
    visualInventory = VisualInventory(INVENTORY)
    func = SearchingAlgorithm(INVENTORY)

    print('=====================================')
    print('         📦STORE INVENTORY📦')
    print('=====================================')

    visualInventory.printInventory()

    while True:
        print('\n--- Searching Menu ---')
        try:
            target_id_str = input(
                'Enter the Product ID you want to search for (or ‘q’ to exit):')
            if target_id_str.lower() == 'q':
                print('Thank you for using the system. See you later!')
                sys.exit()
            target_id = int(target_id_str)
        except ValueError:
            print('Invalid input! Please enter a number.')
            continue

        print('Choose the search algorithm')
        print(' 1. Linear Search')
        print(' 2. Binary Search')
        print(' 3. Interpolation Search')

        while True:
            try:
                choice = int(input('Enter your choice (1/2/3): '))
                break
            except ValueError:
                print('Invalid Input! Please enter a number')

        product_found = None
        step = 0

        start_time = time.perf_counter()

        if choice == 1:
            product_found, step = func.linearSearch(target_id)
        elif choice == 2:
            product_found, step = func.binarySearch(target_id)
        elif choice == 3:
            product_found, step = func.interpretationSearch(target_id)
        else:
            print('Invalid Choice! Try again')
            continue

        end_time = time.perf_counter()

        visualInventory.printProduct(product_found)

        time_ms = (end_time - start_time) * 1000
        print('--- Performance Results ---')
        print(f' Step Total: {step} steps')
        print(f' Execution Time: {time_ms} ms')
        print('---------------------------')

        input('\nPress enter for continue searching')


if __name__ == "__main__":
    main()