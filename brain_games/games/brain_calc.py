import operator
import random

BRAIN_CALC_PROMPT = "What is the result of the expression?"
MIN_NUMBER = 1
MAX_NUMBER = 100


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
    correct_answer = operations[op_symbol](a, b)

    return question, str(correct_answer)
