# Run all python scripts under src
all:
	find src -depth 1 -type f -name "*.py" -exec python {} ";"


# Install or upgrade code formatting dependencies
dev_deps:
	pip install --upgrade black isort


# Format python codes
lint:
	black .
	isort .


# Clean temp or output files
clean:
	find . -type d -name  "__pycache__" -exec rm -r {} +


# Move my leetcode solutions files downloaded
# Tampermonkey script: https://gist.github.com/Roytangrb/7df5bd7c0321debb9df8e539662b08ea
# Posix BRE: https://en.wikibooks.org/wiki/Regular_Expressions/POSIX_Basic_Regular_Expressions
mv_py:
	find ~/Downloads -depth 1 -type f -regex ".*\/[0-9]\{1,4\}[-[:alnum:]]\{1,\}\.py" -exec mv -f -v {} ./leetcode/python ";"


mv_rs:
	find ~/Downloads -depth 1 -type f -regex ".*\/[0-9]\{1,4\}[-[:alnum:]]\{1,\}\.rs" -exec mv -f -v {} ./leetcode/rust ";"
