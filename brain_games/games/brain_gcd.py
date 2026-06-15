import random

BRAIN_GCD_PROMPT = "Find the greatest common divisor of given numbers."
MIN_NUMBER = 1
MAX_NUMBER = 100


def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def brain_gcd_game():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = f"{a} {b}"
    correct_answer = find_gcd(a, b)

    return question, str(correct_answer)
