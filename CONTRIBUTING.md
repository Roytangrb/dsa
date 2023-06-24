# Development Guide

## Getting Started

All scripts and packages are under `src/` directory. You can run the example scripts, i.e., `python src/quickselect.py`.

### Requirements

- `python` (>3.10)
- `cmake`

### Python Setup

The codes are developed using the latest version of python.
The setup does not require using `pyenv`. You can setup or use any of compatible python3 versions.

#### Create Python3 Virtual Environment

```sh
python3 -m venv env
# or below if system python is shimmed by pyenv
python -m venv env
```

#### Config Vscode to auto activate venv

- `Command-Shift-p` to select interpreter: `./env/bin/python`
- Add `"python.terminal.activateEnvironment": true` to `.vscode/settings.json`

### Install Dependencies

```sh
make deps
```

### Lint/Format Code

```sh
make fmt
```

### Build and Open Doc in Browser

```sh
make doc
```
