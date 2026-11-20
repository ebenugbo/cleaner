# Cleaner

A small interactive Python utility for cleaning temporary files and finding large files in your Downloads folder.

## Features

- Clean the Windows temporary folders
- Remove `__pycache__` directories from the current project
- Remove `.pytest_cache` directories
- Scan Downloads for files larger than 100 MB
- Combine temporary-folder and project-cache cleaning in one option
- Report the approximate space freed and number of items removed

## Requirements

- Python 3
- Windows is recommended for the temporary-folder options

No third-party packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/ebenugbo/cleaner.git
cd cleaner
```

## Usage

Run the script from a terminal:

```bash
python cleaner.py
```

You will see an interactive menu:

```text
=== PYTHON SYSTEM CLEANER ===
1. Clean Windows Temp
2. Clean current project (__pycache__, .pycache)
3. Find large files > 100MB in Downloads
4. Full Clean (1+2)
Choose:
```

### Menu options

| Option | Action |
|---|---|
| `1` | Deletes the contents of the Windows TEMP folders |
| `2` | Recursively finds and deletes `__pycache__` directories in the current directory |
| `3` | Lists files over 100 MB in your Downloads folder |
| `4` | Runs options 1 and 2 |

## How it works

- Temporary folders are read from `TEMP` and `LOCALAPPDATA` environment variables.
- Cache directories are discovered relative to the directory where `cleaner.py` is run.
- Files and directories are calculated recursively to estimate freed space.
- Files larger than 100 MB are identified by walking through the Downloads directory.

## Project structure

```text
cleaner/
├── cleaner.py
├── LICENSE
└── README.md
```

## Safety notes

> Temporary and cache folders may contain files currently in use by running programs.

- Review cleanup targets before running the tool.
- Close applications that may be using temporary files.
- Option 3 only reports large files; it does not delete them.
- The cleaner deletes contents rather than asking for confirmation for each item.

## License

This project is licensed under the [MIT License](LICENSE).
