# Get the project name and version from pyproject.toml
NAME:=$(shell awk -F '"' '/^name/ {print $$2; exit}' pyproject.toml)
WHEEL_NAME:=$(subst -,_,$(NAME))
VER:=$(shell awk -F '"' '/^version/ {print $$2}' pyproject.toml)
DIST_TARGZ:=dist/$(WHEEL_NAME)-$(VER).tar.gz
DIST_WHEEL:=dist/$(WHEEL_NAME)-$(VER)-py3-none-any.whl
WWW_DIR:=www

# Default target
help:
	@echo "make develop - Install dependencies"
	@echo "make format - Format all Python code with black"
	@echo "make doc - Build the documentation site"
	@echo "make doc-serve - Serve the documentation site locally"
	@echo "make test - Run tests"
	@echo "make clean - Remove the dist directory"
	@echo "make build - Build a wheel distribuition"
	@echo "make publish - Publish the wheel to Artifactory"
	
develop:
	pip install poetry
	poetry install --all-extras

format:
	black . --line-length=100

$(WWW_DIR): 
	mkdocs build

doc: $(WWW_DIR)

doc-serve:
	mkdocs serve

test:
	pytest tests

clean:
	rm -rf dist || true

$(DIST_TARGZ):
	poetry build -f sdist

$(DIST_WHEEL):
	poetry build -f wheel

build: clean $(DIST_TARGZ) $(DIST_WHEEL)

publish: $(DIST_TARGZ) $(DIST_WHEEL)
	twine upload $(DIST_TARGZ) $(DIST_WHEEL)

.PHONY: help develop format doc doc-serve test clean build publish