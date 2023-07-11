.PHONY: runserver
runserver:
	poetry run python -m src.manage runserver

.PHONY: makemigrations
makemigrations:
	poetry run python -m src.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python -m src.manage migrate

.PHONY: pre-commit-install
pre-commit-install:
	poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: docker-up
docker-up:
	docker-compose -f docker-compose.dev.yaml up -d

.PHONY: docker-down
docker-down:
	docker-compose -f docker-compose.dev.yaml down

.PHONY: draw-diagram
draw-diagram:
	rm -f db_diagram.png
	poetry run python -m src.manage graph_models -a -g --dot -o db_diagram.dot
	poetry run dot -Tpng db_diagram.dot -o db_diagram.png
	rm db_diagram.dot