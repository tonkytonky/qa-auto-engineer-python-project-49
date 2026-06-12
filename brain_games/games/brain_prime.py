import random

from brain_games.constants import MAX_NUMBER, MIN_NUMBER

BRAIN_PRIME_PROMPT = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for d in range(3, int(number**0.5) + 1, 2):
        if number % d == 0:
            return False
    
    return True


def brain_prime_game():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if is_prime(question) else "no"
    return question, correct_answer
