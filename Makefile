PYTHON_FILES ?= .

all: configure format lint-check build

.PHONY: configure
configure:
	poetry install --no-root

# Format files
.PHONY: format
format:
	@echo "Formatting python files"
	poetry run ruff check --fix $(PYTHON_FILES)

# Perform Python ruff check
.PHONY: lint-check
lint-check:
	@echo "Lint check python files"
	poetry run ruff check $(PYTHON_FILES)

# Test the package
.PHONY: test
test:
	@echo "Testing package"
	poetry run pytest

# Build the package
.PHONY: build
build:
	@echo "Building package"
	poetry build

# Upload the package
.PHONY: publish
publish:
	@echo "Uploading package"
	poetry publish
