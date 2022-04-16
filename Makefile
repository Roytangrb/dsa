format_deps:
	# Install or upgrade code formatting dependencies
	pip install --upgrade black isort


format:
	# Format python codes using default
	black .
	isort .
