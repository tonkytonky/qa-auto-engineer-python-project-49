import random

import prompt

from brain_games.cli import welcome_user
from brain_games.constants import CORRECT_ANSWERS, MAX_NUMBER, MIN_NUMBER


def brain_even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < CORRECT_ANSWERS:
        question = random.randint(MIN_NUMBER, MAX_NUMBER)
        is_question_even = question % 2 == 0
        correct_answer = "yes" if is_question_even else "no"

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.")
            return

    print(f"Congratulations, {name}!")
