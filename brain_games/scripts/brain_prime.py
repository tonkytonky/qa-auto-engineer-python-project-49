from brain_games.engine import run_game
from brain_games.games.brain_prime import BRAIN_PRIME_PROMPT, brain_prime_game


def main():
    run_game(brain_prime_game, BRAIN_PRIME_PROMPT)


if __name__ == "__main__":
    main()
