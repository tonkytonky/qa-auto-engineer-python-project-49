import random

from brain_games.constants import MAX_NUMBER, MIN_NUMBER

BRAIN_EVEN_PROMPT = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even_game():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if question % 2 == 0 else "no"
    return question, correct_answer
