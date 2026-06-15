import random

BRAIN_EVEN_PROMPT = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def brain_even_game():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if question % 2 == 0 else "no"

    return str(question), correct_answer
