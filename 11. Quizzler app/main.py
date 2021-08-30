import requests
from quiz_brain import QuizBrain
from question_model import Question

# Get the raw data
parameters = {
    "amount": 10,
    "type": "boolean"
}
res = requests.get("https://opentdb.com/api.php", params=parameters)
res.raise_for_status()
question_data = res.json()["results"]

# Get the cooked data and put it into a list
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_num}")