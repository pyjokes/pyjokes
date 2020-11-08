# vim: set noet sw=4 ts=4 fileencoding=utf-8:

# External utilities
PYTHON=python
PIP=pip
TOX=tox
PYTEST=pytest
TWINE=twine
MKDOCS=mkdocs
PYFLAGS=
DEST_DIR=/

NAME:=$(shell $(PYTHON) $(PYFLAGS) setup.py --name)
VER:=$(shell $(PYTHON) $(PYFLAGS) setup.py --version)

# Calculate the name of all outputs
DIST_WHEEL=dist/$(NAME)-$(VER)-py2.py3-none-any.whl
DIST_TAR=dist/$(NAME)-$(VER).tar.gz

# Default target
all:
	@echo "make install - Install on local system"
	@echo "make develop - Install symlinks for development"
	@echo "make test - Run tests"
	@echo "make doc - Generate HTML and PDF documentation"
	@echo "make sdist - Generate a source tar package"
	@echo "make wheel - Generate a bdist wheel package"
	@echo "make dist - Generate all packages"
	@echo "make clean - Get rid of all generated files"
	@echo "make release - Create and tag a new release"
	@echo "make upload - Upload the new release to PyPI"

install: $(SUBDIRS)
	$(PYTHON) $(PYFLAGS) setup.py install --root $(DEST_DIR)

doc:
	$(MKDOCS) build

source: $(DIST_TAR) $(DIST_ZIP)

wheel: $(DIST_WHEEL)

tar: $(DIST_TAR)

dist: $(DIST_WHEEL) $(DIST_TAR)

develop: tags
	@# These have to be done separately to avoid a cockup...
	$(PIP) install -U setuptools
	$(PIP) install -U pip
	$(PIP) install -e .[doc,test]

test: $(TOX)

clean:
	dh_clean
	rm -fr dist/ $(NAME).egg-info/ tags
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir clean; \
	done

$(SUBDIRS):
	$(MAKE) -C $@

$(DIST_TAR): $(PY_SOURCES) $(SUBDIRS)
	$(PYTHON) $(PYFLAGS) setup.py sdist --formats gztar

$(DIST_WHEEL): $(PY_SOURCES) $(SUBDIRS)
	$(PYTHON) $(PYFLAGS) setup.py bdist_wheel --universal

release: $(DIST_DEB) $(DIST_DSC) $(DIST_TAR) $(DIST_WHEEL)
	git tag -s v$(VER) -m "Release v$(VER)"
	git push --tags
	# build a source archive and upload to PyPI
	$(TWINE) upload $(DIST_TAR) $(DIST_WHEEL)

.PHONY: all install develop test doc sdist wheel tar dist clean tags release upload $(SUBDIRS)
