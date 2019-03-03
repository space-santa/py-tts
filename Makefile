# The Django targets.
.PHONY: mypy
mypy:
	mypy --config-file setup.cfg src

.PHONY: black-check
black-check:
	black --exclude migrations --check src

.PHONY: black
black:
	black --exclude migrations src

.PHONY: isort
isort:
	isort -y --skip env

.PHONY: isort-check
isort-check:
	isort --diff --skip env

.PHONY: flake8
flake8:
	flake8 src

.PHONY: pylint
pylint:
	pylint src

.PHONY: lint
lint : isort-check black-check flake8 pylint mypy
