from src.Sort import Sort
from data.input.data import random_number

def main():
    print('===================================')
    print('            Sorting Data')
    print('===================================')

    print('\n--- Sort ---')
    print(f'Random Data: {random_number}')

    sorted_data = Sort(random_number)

    new_data = sorted_data.quick_sort(random_number)

    print(f'Sorted Data: {new_data}')


if __name__ == "__main__":
    main()