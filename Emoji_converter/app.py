

input_user = input('> ')


def emoji_converter(massage):
    EMOJI = {
        ':)': '😁',
        ':(': '😞'
    }

    word = massage.split()
    output = ''

    for wd in word:
        if wd in EMOJI:
            output += EMOJI.get(wd, wd)
        else:
            output += wd + ' '

    return output


print(emoji_converter(input_user))
