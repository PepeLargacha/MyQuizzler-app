import random

from data import trivia_api_get
from question_model import Question


class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.question_list = None
        self.current_question = None
        self.get_questions_from_api()

    def get_questions_from_api(self):
        question_bank = []
        for question in trivia_api_get():
            question_text = question["question"]
            question_answer = bool(question["correct_answer"])
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)
        self.question_list = question_bank

    def still_has_questions(self):
        return 0 < len(self.question_list)

    def next_question(self):
        rnd_index = random.randint(0, len(self.question_list)-1)
        self.current_question = self.question_list.pop(rnd_index)
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer is correct_answer:
            self.score += 1
            return True
        else:
            return False
