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


cp_py:
	# copy my leetcode solutions files downloaded
	# Tampermonkey script: https://gist.github.com/Roytangrb/7df5bd7c0321debb9df8e539662b08ea
	# BRE Regex: https://en.wikibooks.org/wiki/Regular_Expressions/POSIX_Basic_Regular_Expressions
	find ~/Downloads -depth 1 -type f -regex ".*\/[0-9]\{1,4\}[-[:lower:]]\{1,\}\.py" -exec cp -v {} ./leetcode/python ";"
