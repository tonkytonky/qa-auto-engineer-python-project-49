from brain_games.engine import run_game
from brain_games.games.brain_calc import BRAIN_CALC_PROMPT, brain_calc_game


def main():
    run_game(brain_calc_game, BRAIN_CALC_PROMPT)


if __name__ == "__main__":
    main()
