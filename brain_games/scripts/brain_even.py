from brain_games.engine import run_game
from brain_games.games.brain_even import BRAIN_EVEN_PROMPT, brain_even_game


def main():
    run_game(brain_even_game, BRAIN_EVEN_PROMPT)


if __name__ == "__main__":
    main()
