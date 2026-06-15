from collections.abc import Callable

import prompt

from brain_games.cli import welcome_user

CORRECT_ANSWERS_TO_WIN = 3


def run_game(game_func: Callable[[], tuple[str, str]], game_prompt: str):
    name = welcome_user()
    print(game_prompt)

    correct_answers = 0
    while correct_answers < CORRECT_ANSWERS_TO_WIN:
        question, correct_answer = game_func()

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer was '{correct_answer}'.",
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
