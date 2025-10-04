quiz_success = 0
number_question = 0


def score_quiz(check_result):
    if check_result == 1:
        return 1
    else:
        return 0


def question(question, answer1, answer2, answer3, correct_answer):
    global quiz_success
    global number_question

    number_question += 1

    print(
        f'Question {number_question}: {question}?\na) {answer1}\nb) {answer2}\nc) {answer3}')

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
        quiz_success += 1
    else:
        print('Wrong')
        quiz_success += 0


def main():
    question('What is Capital of France', 'Paris', 'London', 'Rome', 'Paris')
    question('What is Largest Planet in Our Solar Sytem', 'Earth', 'Jupiter', 'Mars', 'Jupiter')
    print(f'Your final score: {quiz_success}/{number_question}')


if __name__ == "__main__":
    main()
