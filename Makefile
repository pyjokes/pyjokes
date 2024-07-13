# Get the project name and version from pyproject.toml
NAME:=$(shell awk -F '"' '/^name/ {print $$2; exit}' pyproject.toml)
WHEEL_NAME:=$(subst -,_,$(NAME))
VER:=$(shell awk -F '"' '/^version/ {print $$2}' pyproject.toml)
DIST_WHEEL:=dist/$(WHEEL_NAME)-$(VER)-py3-none-any.whl

# Default target
help:
	@echo "make develop - Install dependencies"
	@echo "make format - Format all Python code with black"
	@echo "make doc - Build the documentation site"
	@echo "make test - Run tests"
	@echo "make clean - Remove the dist directory"
	@echo "make build - Build a wheel distribuition"
	@echo "make publish - Publish the wheel to Artifactory"
	
develop:
	pip install poetry
	poetry install --all-extras

format:
	black .

test:
	pytest tests

clean:
	rm -rf dist

$(DIST_WHEEL): clean
	poetry build

build: $(DIST_WHEEL)

publish: $(DIST_WHEEL)
	twine upload $(DIST_WHEEL)

.PHONY: help develop format doc test clean build publish