from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank =[]



for i in range(len(question_data)):
    q1 = question_data[i]["text"]
    a1 = question_data[i]["answer"]
    txt = Question(q1,a1)
    question_bank.append(txt)


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
    quiz.check_ans()
print("\n" * 6)
print("*****You have completed your quiz******")
print(f"Your score is {quiz.score}/{len(question_bank)}")

