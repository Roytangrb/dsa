# Run all python scripts under src
.PHONY: all
all:
	find src -depth 1 -type f -name "*.py" -exec python {} ";"


# Install dependencies
.PHONY: deps
deps:
	# Python source code dependencies
	PIP_EXTRA_INDEX_URL= pip install -r requirements.txt
	# Install or upgrade code formatting dependencies
	PIP_EXTRA_INDEX_URL= pip install --upgrade black isort


# Format codes
.PHONY: fmt
fmt:
	@ echo "Formating Python..."
	black .
	isort --skip-glob env/* .
	@ echo "Formating Rust..."
	@ find ./leetcode/rust -type f -name "*.rs" -exec rustfmt {} +


# Clean temp or output files
.PHONY: clean
clean:
	@ find . -type d -name  "__pycache__" -exec rm -r {} +


# Move my leetcode solutions files downloaded
# Tampermonkey script: https://gist.github.com/Roytangrb/7df5bd7c0321debb9df8e539662b08ea
LANGUAGES := python.py rust.rs c.c

# Posix BRE: https://en.wikibooks.org/wiki/Regular_Expressions/POSIX_Basic_Regular_Expressions
LC_FILENAME_REGEX := .*\/[0-9]\{1,4\}[-[:alnum:]]\{1,\}

.PHONY: mv_code $(LANGUAGES)
mv_code: $(LANGUAGES)


.PHONY: $(LANGUAGES)
$(LANGUAGES):
	@ $(MAKE) find_downloaded \
	LANG_NAME=$(word 1,$(subst ., ,$@)) \
	LANG_EXT=$(word 2,$(subst ., ,$@))


.PHONY: find_downloaded
find_downloaded:
	@ echo "Moving $(LANG_NAME) code files ..."
	@ find ~/Downloads -depth 1 -type f -regex "$(LC_FILENAME_REGEX)\.$(LANG_EXT)" -exec mv -f -v {} ./leetcode/$(LANG_NAME) ";"
