# Run all python scripts under src
.PHONY: all
all:
	find src -depth 1 -type f -name "*.py" -exec python {} ";"


# Install or upgrade code formatting dependencies
.PHONY: dev_deps
dev_deps:
	pip install --upgrade black isort


# Format python codes
.PHONY: lint
lint:
	black .
	isort .


# Clean temp or output files
.PHONY: clean
clean:
	find . -type d -name  "__pycache__" -exec rm -r {} +


# Move my leetcode solutions files downloaded
# Tampermonkey script: https://gist.github.com/Roytangrb/7df5bd7c0321debb9df8e539662b08ea
.PHONY: mv_code
mv_code: mv_py mv_rs


# Posix BRE: https://en.wikibooks.org/wiki/Regular_Expressions/POSIX_Basic_Regular_Expressions
LC_FILENAME_REGEX := .*\/[0-9]\{1,4\}[-[:alnum:]]\{1,\}


.PHONY: mv_py
mv_py:
	find ~/Downloads -depth 1 -type f -regex "$(LC_FILENAME_REGEX)\.py" -exec mv -f -v {} ./leetcode/python ";"


.PHONY: mv_rs
mv_rs:
	find ~/Downloads -depth 1 -type f -regex "$(LC_FILENAME_REGEX)\.rs" -exec mv -f -v {} ./leetcode/rust ";"
