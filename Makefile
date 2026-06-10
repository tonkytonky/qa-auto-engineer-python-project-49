install:
	uv sync

build:
	uv build

lint:
	uv run ruff check brain_games

package-install: build
	uv tool install dist/*.whl

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

.PHONY: install build lint package-install brain-games
