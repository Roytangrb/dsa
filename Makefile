all:
	# Run all scripts under src
	find src -depth 1 -type f -name "*.py" -exec python {} ";"


dev_deps:
	# Install or upgrade code formatting dependencies
	pip install --upgrade black isort


lint:
	# Format python codes using default
	black .
	isort .


clean:
	find . -type d -name  "__pycache__" -exec rm -r {} +
