from question_model import Question
from data import question_data


def create_questions():
    question_bank = []
    for question in question_data:
        new_question = Question(text=question["text"], answer=question["answer"])
        question_bank.append(new_question)
    return question_bank

