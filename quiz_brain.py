class QuizBrain:
    def __init__(self,list):
        self.question_no =0
        self.question_list = list
        self.score =0

    def still_has_qs(self):
        if len(self.question_list) > self.question_no:
            return True
        else:
            return False


    def next_q(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer =input(f"q.{self.question_no} :{current_question.text}(yes/no)?")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right")
            self.score += 1
        else:
            print("sorry..its wrong")
            print(f"correct answer is {correct_answer}")

        print(f"your score is {self.score}/{self.question_no}\n")
