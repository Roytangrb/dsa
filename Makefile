dev_deps:
	# Install or upgrade code formatting dependencies
	pip install --upgrade black isort


lint:
	# Format python codes using default
	black .
	isort .

clean:
	find . -type d -name  "__pycache__" -exec rm -r {} +
