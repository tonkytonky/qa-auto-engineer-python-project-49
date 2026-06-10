import prompt

import brain_games.constants as c
from brain_games.cli import welcome_user
from brain_games.games.brain_calc import BRAIN_CALC_PROMPT, brain_calc_game
from brain_games.games.brain_even import BRAIN_EVEN_PROMPT, brain_even_game


def run_game(name, game_greeting, game):
    print(game_greeting)

    correct_answers = 0
    while correct_answers < c.CORRECT_ANSWERS_TO_WIN:
        question, correct_answer = game()

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
            return

    print(f"Congratulations, {name}!")


def engine(game_choice):
    name = welcome_user()

    match game_choice:
        case c.BRAIN_EVEN_NAME:
            run_game(name, BRAIN_EVEN_PROMPT, brain_even_game)
        case c.BRAIN_CALC_NAME:
            run_game(name, BRAIN_CALC_PROMPT, brain_calc_game)
