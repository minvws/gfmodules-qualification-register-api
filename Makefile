NEW_UID = 1000
NEW_GID = 1000

ifdef DOCKER
  RUN_PREFIX := docker compose run --rm app
else
  RUN_PREFIX :=
endif

.SILENT: help
all: help

autopilot: ## Runs the autopilot script for no-config setup of the project
	./tools/autopilot.sh

container-build: ## Build the container
	docker compose build --build-arg="NEW_UID=${NEW_UID}" --build-arg="NEW_GID=${NEW_GID}"

up: ## Start the container
	docker compose up

bash: ## Runs a bash prompt inside the container
	docker compose run --rm register-api bash

lint: ## Check for linting errors
	$(RUN_PREFIX) ruff check

lint-fix: ## Fix linting errors
	$(RUN_PREFIX) ruff check --fix --show-fixes

type-check: ## Check for typing errors
	$(RUN_PREFIX) mypy app

safety-check: ## Check for security vulnerabilities
	$(RUN_PREFIX) safety check

spelling-check: ## Check spelling mistakes
	$(RUN_PREFIX) codespell . --ignore-words=codespell-ignore.txt

spelling-fix: ## Fix spelling mistakes
	$(RUN_PREFIX) codespell . --write-changes --interactive=3  --ignore-words=codespell-ignore.txt

test: ## Runs automated tests
	$(RUN_PREFIX) pytest --cov

check: lint type-check safety-check spelling-check test ## Runs all checks
fix: lint-fix spelling-fix ## Runs all fixers

help: ## Display available commands
	echo "Available make commands:"
	echo
	grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-30s\033[0m %s\n", $$1, $$2}'
