# Coding Challenge WC Tool

This is a simple CLI tool to count words, lines, and characters in a text file to replicate the behavior of wc.

## Prerequisites

- Python 3.8 or higher
- [Poetry](https://python-poetry.org/) for dependency management

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/coding-challenge-wc-tool.git
    cd coding-challenge-wc-tool
    ```

2. Install dependencies using Poetry:

    ```sh
    poetry install
    ```

## Usage

1. Activate the virtual environment and install the package:

    ```sh
    poetry shell
    pip install --editable .
    ```

2. Run the CLI tool:

    ```sh
    ccwc <command> --f <path_to_text_file>
    ```

    Replace `<path_to_text_file>` with the path to the text file you want to analyze.

    Available commands:
    ``` sh
    ccwc count --f <path_to_text_file> #- Count the number of bytes in the file.
    ccwc line --f <path_to_text_file> #- Count the number of lines in the file.
    ccwc word --f <path_to_text_file> #- Count the number of words in the file.
    ccwc char --f <path_to_text_file> #- Count the number of characters in the file.
    ccwc <path_to_text_file> #- Count the number of words, lines, and characters in the file.
    ``` 

## Example

```sh
ccwc example.txt
```

This will output the number of words, lines, and characters in `example.txt`.
