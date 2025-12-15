# =========================
# Project configuration
# =========================

PROJECT_NAME = bookstore
SERVICE_WEB = web
PYTHON_VERSION = 3.10

# =========================
# Helpers
# =========================

DOCKER_COMPOSE = docker compose
EXEC_WEB = $(DOCKER_COMPOSE) exec $(SERVICE_WEB)

COLOR_GREEN = \033[32m
COLOR_YELLOW = \033[33m
COLOR_RESET = \033[0m

##@ Help

.PHONY: help
help:
	@echo ""
	@echo "Available commands:"
	@echo ""
	@echo "  make up               Build and start containers"
	@echo "  make down             Stop containers"
	@echo "  make down-v           Stop containers and remove volumes"
	@echo "  make logs             Show web logs"
	@echo "  make ps               List containers"
	@echo ""
	@echo "  make migrate          Run Django migrations"
	@echo "  make makemigrations   Create Django migrations"
	@echo "  make createsuperuser  Create Django superuser"
	@echo ""
	@echo "  make test             Run tests"
	@echo "  make check            Run linters"
	@echo "  make format           Format code"
	@echo ""


##@ Docker

.PHONY: up
up: ## Build and start containers
	$(DOCKER_COMPOSE) up -d --build

.PHONY: down
down: ## Stop containers
	$(DOCKER_COMPOSE) down

.PHONY: down-v
down-v: ## Stop containers and remove volumes
	$(DOCKER_COMPOSE) down -v

.PHONY: logs
logs: ## Show logs from web container
	$(DOCKER_COMPOSE) logs -f $(SERVICE_WEB)

.PHONY: ps
ps: ## List containers
	$(DOCKER_COMPOSE) ps

##@ Django

.PHONY: migrate
migrate: ## Run Django migrations
	$(EXEC_WEB) python manage.py migrate

.PHONY: makemigrations
makemigrations: ## Create Django migrations
	$(EXEC_WEB) python manage.py makemigrations

.PHONY: createsuperuser
createsuperuser: ## Create Django superuser
	$(EXEC_WEB) python manage.py createsuperuser

.PHONY: shell
shell: ## Open Django shell
	$(EXEC_WEB) python manage.py shell

##@ Tests & Quality

.PHONY: test
test: ## Run tests with pytest
	$(EXEC_WEB) pytest

.PHONY: check
check: ## Run linters locally with Poetry
	poetry run flake8 .
	poetry run black --check .
	poetry run mypy .

.PHONY: format
format: ## Format code locally with Poetry
	poetry run black .
	poetry run isort .

##@ Poetry

.PHONY: lock
lock: ## Regenerate poetry.lock
	$(EXEC_WEB) poetry lock

.PHONY: deps
deps: ## Install dependencies via Poetry
	$(EXEC_WEB) poetry install

##@ Maintenance

.PHONY: clean
clean: ## Remove containers, volumes and cache
	$(DOCKER_COMPOSE) down -v --remove-orphans
