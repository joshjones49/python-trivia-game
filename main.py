import random

questions = {
    "What is the keyword to define a function in Python?": "def",
    "What is the output of print(type({}))?": "dict",
    "Which data type is used to store True/False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "What function is used to get input from the user?": "input()",
    "What symbol is used to comment in Python?": "#",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}

def check_score(score):
    if score == 0:
        print("You failed: :(")
    elif 0 < score < 3:
        print("You did ok but need to improve")
    elif 3 <= score < 5:
        print("Good Job :)")
    else:
        print("Perfect Score!")


def trivia_game():
    question_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(question_list, total_questions)
    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your Answer: ").lower().strip() #.strip() removes white space
        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
            print(f"Score: {score}/{total_questions}")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}.\n")
            print(f"Score: {score}/{total_questions}")

    check_score(score)


trivia_game()
