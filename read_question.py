import csv
import question_list



def read_questions_from_csv(filename):
    question = []
    with open('question_list.' + filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            question.append(row)
        return question
