import random

from brain_games.constants import MAX_NUMBER, MIN_NUMBER

BRAIN_GCD_PROMPT = "Find the greatest common divisor of given numbers."


def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def brain_gcd_game():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = f"{a} {b}"
    correct_answer = str(find_gcd(a, b))

    return question, correct_answer
