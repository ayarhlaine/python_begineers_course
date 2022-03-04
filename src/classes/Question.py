class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def check_answer(self, answer):
        return answer == self.answer
