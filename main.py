import modules as modules
import read_question as read_question


def geography():
    modules.ask_question('What is Capital of France',
                          'Paris', 'London', 'Rome', 'Paris')
    modules.ask_question('What is Largest Planet in Our Solar Sytem',
                          'Earth', 'Jupiter', 'Mars', 'Jupiter')


def geo_difficult():
    modules.ask_question('Which of these countries is a true enclave, entirely surrounded by the territory of just one other nation?',
                          'Switzerland', 'Lesotho', 'Bhutan', 'Lesotho')
    modules.ask_question('While the Atacama is the driest hot desert, what is considered the overall driest place on Earth, located in Antarctica?',
                          'Death Valley', 'The Sahara Desert', 'The McMurdo Dry Valleys', 'The McMurdo Dry Valleys')


def history():
    modules.ask_question(
        'In what year did Indonesia proclaim its independence?', '1942', '1945', '1949', '1945')
    modules.ask_question('The Battle of Surabaya, a symbol of Indonesian resistance, is commemorated annually on which date?',
                          'August 17', 'October 28', 'November 10', 'November 10')


def his_difficult():
    modules.ask_question('The climax of the Battle of Surabaya on Nov 10, 1945 was triggered by the death of a British officer. Who was this Brigadier?',
                          'Lord Mountbatten', 'Sir Philip Christison', 'A.W.S. Mallaby', 'A.W.S. Mallaby')
    modules.ask_question('Recorded as the shortest war in history, the Anglo-Zanzibar War of 1896 lasted for approximately how long?',
                          'Two Days', 'Six Hours', '38 Minutes', '38 Minutes')


def science():
    modules.ask_question('What is the process where plants make their own food using sunlight?',
                          'Respiration', 'Photosynthesis', 'Transpiration', 'Photosynthesis')
    modules.ask_question("What is the most abundant gas in the Earth's atmosphere?",
                          'Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Nitrogen')


def sci_difficult():
    modules.ask_question('What is the name of the counter-intuitive phenomenon where, under certain conditions, hot water can freeze faster than cold water?',
                          'The Leidenfrost Effect', 'The Mpemba Effect', 'The Peltier Effect', 'The Mpemba Effect')
    modules.ask_question('The blue whale is the largest animal. However, what is considered the largest single living organism on Earth by area?',
                          'The Great Barrier Reef', 'A fungus (Armillaria ostoyae)', 'General Sherman (Giant Sequoia tree)', 'A fungus (Armillaria ostoyae)')


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
                all_question = read_question.read_questions_from_csv('geography.csv')
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
                geo_difficult()
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
                history()
                break
            elif quiz_difficulty == 2:
                his_difficult()
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
                science()
                break
            elif quiz_difficulty == 2:
                sci_difficult()
                break
            else:
                print('Please select 1 or 2')
        else:
            print('Invalid Choice')

    print(
        f'Your final score: {modules.success() - 1}/{modules.increment_question_count() - 1}')


if __name__ == "__main__":
    main()
