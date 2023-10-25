from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def create_questions():
    question_bank = []
    for question in question_data:
        new_question = Question(text=question["text"], answer=question["answer"])
        question_bank.append(new_question)
    brain = QuizBrain(question_bank)
    return brain


def quiz():
    questions = create_questions()
    while questions.still_has_questions():
        questions.next_question()
    print("You've completed the quiz!")
    print(f"Your final score is: {questions.score}/{questions.question_number}.")


quiz()
