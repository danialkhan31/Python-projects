
class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        global current_question
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        global user_ans
        user_ans = input(f"Q.{self.question_number} : {current_question.text}?(True or False).").title()


    def check_ans(self):
        if user_ans == current_question.ans:
            self.score +=1
            print("you are right...")
            print("Your Score is :" ,self.score ,"/",self.question_number)
        else:
            print("Hmmm You are wrong .....")
            print("Your Score is :", self.score, "...")
        print(f"The correct ans was : {current_question.ans} \nand your score is {self.score}/{self.question_number}. ")





