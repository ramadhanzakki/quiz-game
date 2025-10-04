quiz_success = 0
number_question = 0


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


def geography():
    question('What is Capital of France', 'Paris', 'London', 'Rome', 'Paris')
    question('What is Largest Planet in Our Solar Sytem', 'Earth', 'Jupiter', 'Mars', 'Jupiter')


def history():
    question('In what year did Indonesia proclaim its independence?', '1942', '1945', '1949', '1945')
    question('The Battle of Surabaya, a symbol of Indonesian resistance, is commemorated annually on which date?', 'August 17', 'October 28', 'November 10', 'November 10')


def science():
    question('What is the process where plants make their own food using sunlight?', 'Respiration', 'Photosynthesis', 'Transpiration', 'Photosynthesis')
    question("What is the most abundant gas in the Earth's atmosphere?", 'Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Nitrogen')


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
            geography()
            break
        elif user_input == 2:
            history()
            break
        elif user_input == 3:
            science()
            break
        else:
            print('Invalid Choice')

    print(f'Your final score: {quiz_success}/{number_question}')


if __name__ == "__main__":
    main()
