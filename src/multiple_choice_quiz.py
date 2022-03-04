from classes.Question import Question

question_prompts = [
    "What color are apples?\n (a) Red/Green\n (b) Purple\n (c) Blue\n",
    "What color are Bananas?\n (a) Blue\n (b) Yellow\n (c) Red\n",
]

questions_data = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b")
]


def run_tests(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if question.check_answer(answer):
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")


run_tests(questions_data);
