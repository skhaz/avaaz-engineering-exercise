.PHONY: help run tests vet

.SILENT:

SHELL := bash -eou pipefail

export PYTHONPATH=.

ifeq ($(shell command -v docker-compose;),)
	COMPOSE := docker compose
else
	COMPOSE := docker-compose
endif

help:
	awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: ## Setup everything
	-rm -rf venv
	python3 -m venv venv
	source venv/bin/activate
	pip install -r app/requirements-dev.txt

run: ## Run the project using docker-compose
	$(COMPOSE) up --build

tests: vet ## Run tests
	pytest --cov=app --cov-report html

vet: ## Run linters, type-checking, auto-formaters, and other tools
	black app/
	ruff app/
	isort app/
