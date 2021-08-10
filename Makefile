.DEFAULT_GOLA := help

.PHONY: help
help:
	@awk 'BEGIN {FS = ":"} /^[a-zA-Z]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' ${MAKEFILE_LIST}

.PHONY: test
test: ## Start the test's task
	@coverage run -m pytest test/
	@coverage html -d report_html
	@coverage report

.PHONY: style
style: ## Clean the code with black and isort
	@black app
	@black main.py
	@black test
	@isort app
	@isort main.py
	@isort test

.PHONY: upDocker
upDocker: ## Start a docker container(s)
	@docker build . -t app/flask
	@docker run -dp 8080:8080 app/flask

.PHONY: stopDocker
stopDocker: ## Stop a docker container(s)
	@docker stop $$(docker container ls -aq)

.PHONY: delDocker
delDocker: ## WARNING! Delete all docker container(s)
	@docker stop $$(docker container ls -aq)
	@docker container rm $$(docker container ls -aq)