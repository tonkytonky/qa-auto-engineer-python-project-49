from brain_games.engine import run_game
from brain_games.games.brain_progression import (
    BRAIN_PROGRESSION_PROMPT,
    brain_progression_game,
)


def main():
    run_game(brain_progression_game, BRAIN_PROGRESSION_PROMPT)


if __name__ == "__main__":
    main()
