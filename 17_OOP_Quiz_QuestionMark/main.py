from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def main():
    questions = create_question_bank()
    quiz_brain = QuizBrain(questions)
    
    while quiz_brain.still_has_questions():
        quiz_brain.get_question()
        quiz_brain.get_next_question()

    print("[Quiz] Quiz game is finished!")
    print(f"[Quiz] Your final score was {quiz_brain.player_score}/{len(questions)}")
    return

def create_question_bank():
    question_bank = []

    for q in question_data:
        question_bank.append(Question(q["text"], q["answer"]))
    
    return question_bank

main()