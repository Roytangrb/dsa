format_deps:
	# Install or upgrade code formatting dependencies
	pip install --upgrade black isort


format:
	# Format python codes using default
	black .
	isort .

clean:
	find . -type d -name  "__pycache__" -exec rm -r {} +
