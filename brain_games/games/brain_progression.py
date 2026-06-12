import random

BRAIN_PROGRESSION_PROMPT = "What number is missing in the progression?"
START_FROM = 1
START_TO = 25
STEP_FROM = 1
STEP_TO = 10
LENGTH_FROM = 5
LENGTH_TO = 10


def create_progression(start, step, length):
    return [str(start + index * step) for index in range(length)]


def brain_progression_game():
    start = random.randint(START_FROM, START_TO)
    step = random.randint(STEP_FROM, STEP_TO)
    length = random.randint(LENGTH_FROM, LENGTH_TO)

    question = create_progression(start, step, length)
    hide_at_index = random.randint(0, length - 1)

    correct_answer = question[hide_at_index]
    question[hide_at_index] = ".."
    question = " ".join(question)

    return question, correct_answer
