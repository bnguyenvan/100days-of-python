from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_now = Question(question["text"], question["answer"])
    question_bank.append(question_now)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print(f"You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
