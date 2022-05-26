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


mv_py:
	# Move my leetcode solutions files downloaded
	# Tampermonkey script: https://gist.github.com/Roytangrb/7df5bd7c0321debb9df8e539662b08ea
	# Posix BRE: https://en.wikibooks.org/wiki/Regular_Expressions/POSIX_Basic_Regular_Expressions
	find ~/Downloads -depth 1 -type f -regex ".*\/[0-9]\{1,4\}[-[:alnum:]]\{1,\}\.py" -exec mv -f -v {} ./leetcode/python ";"
