quiz_success = 0
number_question = 0


def success():
    global quiz_success
    quiz_success += 1
    return quiz_success


def increment_question_count():
    global number_question 
    number_question += 1
    return number_question


def ask_question(question, answer1, answer2, answer3, correct_answer):
    number = increment_question_count()

    print(
        f'Question {number}: {question}?\na) {answer1}\nb) {answer2}\nc) {answer3}')

    while True:
        user_answer = input('Your answer: ').lower()
        if user_answer == 'a' or user_answer == 'b' or user_answer == 'c':
            break
        else:
            print('\nWARNING: Please answer a, b, or c')
            continue

    answer = ''
    if user_answer == 'a':
        answer += answer1
    elif user_answer == 'b':
        answer += answer2
    else:
        answer += answer3

    if answer == correct_answer:
        print('Correct')
        success()
    else:
        print('Wrong')
