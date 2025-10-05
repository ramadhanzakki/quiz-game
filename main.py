import question


def geography():
    question.ask_question('What is Capital of France', 'Paris', 'London', 'Rome', 'Paris')
    question.ask_question('What is Largest Planet in Our Solar Sytem', 'Earth', 'Jupiter', 'Mars', 'Jupiter')


def history():
    question.ask_question('In what year did Indonesia proclaim its independence?', '1942', '1945', '1949', '1945')
    question.ask_question('The Battle of Surabaya, a symbol of Indonesian resistance, is commemorated annually on which date?', 'August 17', 'October 28', 'November 10', 'November 10')


def science():
    question.ask_question('What is the process where plants make their own food using sunlight?', 'Respiration', 'Photosynthesis', 'Transpiration', 'Photosynthesis')
    question.ask_question("What is the most abundant gas in the Earth's atmosphere?", 'Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Nitrogen')


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

    print(f'Your final score: {question.success() - 1}/{question.increment_question_count() - 1}')


if __name__ == "__main__":
    main()
