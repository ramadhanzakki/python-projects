NUM_TRANSLATE = {
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven"
}

input_number = input('Phone: ')
translate_number = ''

for ch in input_number:
  translate_number += NUM_TRANSLATE.get(ch) + ' '


print(translate_number)
