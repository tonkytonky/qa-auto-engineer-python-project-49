from brain_games.engine import run_game
from brain_games.games.brain_gcd import BRAIN_GCD_PROMPT, brain_gcd_game


def main():
    run_game(brain_gcd_game, BRAIN_GCD_PROMPT)


if __name__ == "__main__":
    main()
