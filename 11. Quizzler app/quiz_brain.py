import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 1
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    # Check if there are more questions in the list
    def still_has_question(self):
        return self.question_num < len(self.question_list)

    # Head to the next question
    def next_question(self):
        self.current_question = self.question_list[self.question_num - 1]
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_num}: {q_text}"
        # user_answer = input(f"Q.{self.question_num}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    # Check if the user's answer is correct
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
