# HELP

.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

run-server: ## Run docker-compose up as deamon
	docker-compose up -d

run-server-build: ## Run Server build
	docker-compose up -d --build

stop-server: ## Stop Server
	docker-compose down

migrate: ## Run the migrate inside the container
	docker-compose run --rm web python manage.py migrate

collectstatic: ## Run collectstatic script inside the container
	docker-compose run --rm web python manage.py collectstatic --no-input

makemigrations: ## Run the makemigrations inside the container
	docker-compose run --rm web python manage.py makemigrations

test: ## Run Tests in container
	docker-compose run --rm web python manage.py test

create-superuser: ## Create superuser
	docker-compose run --rm web python manage.py createsuperuser

file_change_owner: ## Change file ownership
	sudo chown ${USER}:${USER} -R .

restart_web: ## restart web
	docker-compose restart web