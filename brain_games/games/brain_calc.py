import operator
import random

from brain_games.constants import MAX_NUMBER, MIN_NUMBER

BRAIN_CALC_PROMPT = "What is the result of the expression?"


def brain_calc_game():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)

    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    op_symbol = random.choice(list(operations.keys()))

    question = f"{a} {op_symbol} {b}"
    correct_answer = str(operations[op_symbol](a, b))

    return question, correct_answer
