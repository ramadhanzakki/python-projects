from src.Sort import Sort
from data.input.data import random_number

def main():
    print('===================================')
    print('            Sorting Data')
    print('===================================')

    print('\n---Bubble Sort---')
    print(f'Random Data: {random_number}')

    sorted_data = Sort(random_number)

    sorted_data.insertion_sort()

    print(f'Sorted Data: {random_number}')


if __name__ == "__main__":
    main()