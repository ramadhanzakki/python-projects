import os


def create(filename: str):
    with open(filename, 'w') as file:
        file.write('')


def read(filename: str):
    with open(filename, 'r') as file:
        return file.read()


def write(filename: str, text: str):
    with open(filename, 'w') as file:
        file.write(f'{text}\n')


def add(filename: str, text: str):
    with open(filename, 'a') as file:
        file.write(f'{text}\n')


def replace(filename: str, old_text: str, new_text: str):
    content = read(filename)
    if old_text in content:
        content = content.replace(old_text,new_text)
        print(f'All occurrences of "{old_text}" have been replaced with "{new_text}".')
    else:
        print(f'"{old_text}" isn\'t found in {filename}')
    return content


def main():
    still_writing = True

    file_name = input('Enter the file name to open or create: ')

    if not os.path.exists(file_name):
        print(f'{file_name} not found. Creating a new file.')
        create(file_name)

    while True:
        user_choice = input('overwrite the existing file content, append new text to the end of the file, or edit text in the fie content (W/A/E): ').upper()

        if user_choice == 'W':
            print('Enter your text (type "SAVE" on the new line to save and exit)')

            while still_writing:
                input_text = input()
                if input_text == 'SAVE':
                    still_writing = False
                else:
                    write(file_name, input_text)

            print(f'file {file_name} saved')
            break

        elif user_choice == 'A':
            print('Enter your text (type "SAVE" on the new line to save and exit)')

            while still_writing:
                input_text = input()
                if input_text == 'SAVE':
                    still_writing = False
                else:
                    add(file_name, input_text)

            print(f'file {file_name} saved')
            break
        
        elif user_choice == 'E':
            print(read(file_name))

            old_word = input("Enter the word or phrase to replace: ")
            new_word = input("Enter the new word or phrase: ")

            new_text = replace(file_name, old_word, new_word)
            write(file_name, new_text)
            break
            
        else:
            print('ErrorValue: Enter W or A')




if __name__ == "__main__":
    main()
