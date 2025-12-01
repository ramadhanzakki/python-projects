def length_checker(word):
    if len(word) > 8:
        return 1
    return 0
    

def uppercase_checker(word):
    for char in word:
        if char.isupper():
            return 1
    return 0
        

def digit_checker(word):
    for char in word:
        if char.isdigit():
            return 1
    return 0
        

def special_char_checker(word):
    operator = '@#$%&!'

    for char in word:
        if char in operator:
            return 1
    return 0

def main():
    # Score initialitation
    score = 0
    pass_decision = ''
    feedback = []

    # Input user
    password = input('Enter your password : ')

    # evaluation phase
    score = length_checker(password) + uppercase_checker(password) + digit_checker(password) + special_char_checker(password)

    # Feedback password
    if length_checker(password) == 0:
        feedback.append('Password is too short')

    if uppercase_checker(password) == 0:
        feedback.append('Add a capital letter')

    if digit_checker(password) == 0:
        feedback.append('Add a number')

    if special_char_checker(password) == 0:
        feedback.append('Add unique characters')

    # Decision stage
    if score <= 1:
        pass_decision = 'Very Weak'
    elif score == 2:
        pass_decision = 'Weak'
    elif score == 3:
        pass_decision = 'Medium'
    elif score == 4:
        pass_decision = 'Strong'
    else:
        pass_decision = 'Very Strong'
    
    # Print the decision
    print(f'Password strength : {pass_decision}')

    # Give user the feedback
    if score < 4:
        print(f'Advice for strengthening your password:')
        for item in feedback: print(f'- {item}')


if __name__ == "__main__":
    main()