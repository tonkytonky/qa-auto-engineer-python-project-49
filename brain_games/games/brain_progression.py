import random

BRAIN_PROGRESSION_PROMPT = "What number is missing in the progression?"


def create_progression(start, step, length):
    return [str(start + index * step) for index in range(length)]


def brain_progression_game():
    start = random.randint(1, 25)
    step = random.randint(1, 10)
    length = random.randint(5, 10)

    question = create_progression(start, step, length)
    hide_at_index = random.randint(0, length - 1)

    correct_answer = question[hide_at_index]
    question[hide_at_index] = ".."
    question = " ".join(question)

    return question, correct_answer
