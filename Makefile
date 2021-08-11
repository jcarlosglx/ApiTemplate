.DEFAULT_GOLA := help

.PHONY: help
help: ## Show all the commands
	@awk 'BEGIN {FS = ":"} /^[a-zA-Z]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' ${MAKEFILE_LIST}

.PHONY: test
testApp: ## Start the suit of test for the app
	@coverage run -m pytest test/
	@coverage html -d report_html
	@coverage report

.PHONY: upApp
upApp: ## Star the app
	@python main.py run_server

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
	@docker build -f Dockerfile -t flask-rest:latest .
	@docker run -dp 8080:8080 flask-rest:latest

.PHONY: imgDocker
imgDocker: ## Create only the docker img
	@docker build -f Dockerfile -t flask-rest:latest .

.PHONY: stopDocker
stopDocker: ## Stop a docker container(s)
	@docker stop $$(docker container ls -aq)

.PHONY: delDocker
delDocker: ## WARNING! Delete all docker container(s)
	@docker stop $$(docker container ls -aq)
	@docker container rm $$(docker container ls -aq)

.PHONY: upK8s
upK8s: ## Star a K8s pod (test/dev only)
	@kubectl apply -f k8s/deployment.yaml

.PHONY: delK8s
delK8s: ## Delete a K8s pod
	@kubectl delete -f k8s/deployment.yaml

.PHNOY: upMini
upMini: ## Start the Minikube Cluster
	@minikube start --driver=docker
	@eval $$(minikube docker-env)
	@docker build -f Dockerfile -t flask-rest:latest .
	@kubectl apply -f k8s/deployment.yaml

.PHONY: delMini
delMini: ## WARNING! Delete the Minikube Cluster
	@minikube stop
	@minikube delete

.PHONY: dabodMini
daboMini: ## Show the dashboard of Minikube Cluster
	@minikube dashboard