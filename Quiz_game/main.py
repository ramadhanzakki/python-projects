import modules as modules
import read_question as read_question


def main():
    print('===============================================')
    print('             WELCOME TO MID YEAR EXAM          ')
    print('===============================================')
    print('Today Exam Material:\n1. Geography\n2. History\n3. Science')

    while True:
        try:
            user_input = int(input('Choice the material: '))
        except ValueError:
            print('Enter a number')
            continue

        if user_input == 1:
            print(f'\n--- GEOGRAPHY ---')
            print(f'Select difficulty:\n1) Easy\n2) Hard')

            while True:
                try:
                    quiz_difficulty = int(input('Your choice: '))
                    break
                except ValueError:
                    print('Please select 1 or 2')
                    continue    

            if quiz_difficulty == 1:
                all_question = read_question.read_questions_from_csv('question_list/geography.csv')
                for q in all_question:
                    modules.ask_question(
                        q['question'],
                        q['answer1'],
                        q['answer2'],
                        q['answer3'],
                        q['correct_answer']
                    )
                break
            elif quiz_difficulty == 2:
                all_question = read_question.read_questions_from_csv('question_list/geography_difficulty.csv')
                for q in all_question:
                    modules.ask_question(
                        q['question'],
                        q['answer1'],
                        q['answer2'],
                        q['answer3'],
                        q['correct_answer']
                    )
                break
            else:
                print('Please select 1 or 2')

        elif user_input == 2:
            print(f'\n--- HISTORY ---')
            print(f'Select difficulty:\n1) Easy\n2) Hard')

            while True:
                try:
                    quiz_difficulty = int(input('Your choice: '))
                    break
                except ValueError:
                    print('Please select 1 or 2')
                    continue

            if quiz_difficulty == 1:
                all_question = read_question.read_questions_from_csv('question_list/history.csv')
                for q in all_question:
                    modules.ask_question(
                        q['question'],
                        q['answer1'],
                        q['answer2'],
                        q['answer3'],
                        q['correct_answer']
                    )
                break
            elif quiz_difficulty == 2:
                all_question = read_question.read_questions_from_csv('question_list/history_difficulty.csv')
                for q in all_question:
                    modules.ask_question(
                        q['question'],
                        q['answer1'],
                        q['answer2'],
                        q['answer3'],
                        q['correct_answer']
                    )
                break
            else:
                print('Please select 1 or 2')

        elif user_input == 3:
            print(f'\n--- SCIENCE ---')
            print(f'Select difficulty:\n1) Easy\n2) Hard')

            while True:
                try:
                    quiz_difficulty = int(input('Your choice: '))
                    break
                except ValueError:
                    print('Please select 1 or 2')
                    continue

            if quiz_difficulty == 1:
                all_question = read_question.read_questions_from_csv('question_list/science.csv')
                for q in all_question:
                    modules.ask_question(
                        q['question'],
                        q['answer1'],
                        q['answer2'],
                        q['answer3'],
                        q['correct_answer']
                    )
                break
            elif quiz_difficulty == 2:
                all_question = read_question.read_questions_from_csv('question_list/science_difficulty.csv')
                for q in all_question:
                    modules.ask_question(
                        q['question'],
                        q['answer1'],
                        q['answer2'],
                        q['answer3'],
                        q['correct_answer']
                    )
                break
            else:
                print('Please select 1 or 2')
        else:
            print('Invalid Choice')

    print(
        f'Your final score: {modules.success() - 1}/{modules.increment_question_count() - 1}')


if __name__ == "__main__":
    main()
