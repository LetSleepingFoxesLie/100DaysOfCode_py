class QuizBrain:
    
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.player_score = 0
        self.question_list = question_list
    
    def check_answer(self, question, player_answer):
        print(f"The correct answer was {question.answer}")
        if player_answer.lower() == question.answer.lower():
            print("You got it right! :)")
            self.player_score += 1
        else:
            print("You got it wrong! :/")
        print(f"Your current score: {self.player_score}/{self.question_number + 1}")
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def get_question(self):
        question = self.question_list[self.question_number]
        player_answer = input(f"[Question {self.question_number + 1}] {question.text} [True] or [False]? ")
        self.check_answer(question, player_answer)
    
    def get_next_question(self):
        self.question_number += 1