# Coding Agent and Calculator

A command-line AI coding agent that uses OpenRouter to answer prompts and work with files in the included `calculator/` project. The agent can list and read files, write files, and run Python scripts in its configured working directory.

## Requirements

- Python 3.14 or newer
- An OpenRouter API key

## Setup

Install the dependencies:

```bash
python -m pip install openai==2.44.0 python-dotenv==1.1.0
```

Create a `.env` file in the project root and add your OpenRouter API key:

```env
OPENROUTER_API_KEY=your_api_key_here
```

## Run the Agent

From the project root, provide a prompt as a command-line argument:

```bash
python main.py "What files are in this project?"
```

Use `--verbose` to display prompt and response token counts:

```bash
python main.py --verbose "Explain how the calculator works"
```

The agent uses the `openrouter/free` model and allows up to 20 tool-call iterations for each prompt.

## Available Tools

The agent can:

- List files and directories
- Read file contents, up to 10,000 characters
- Write or overwrite files
- Run Python files with a 30-second timeout

Tool paths are relative to the `calculator/` directory. The path checks reject paths outside that directory.

> **Security:** The agent can write files and execute Python code in `calculator/`. Path checks restrict the file paths passed to its tools, but executing Python is not a security sandbox. Code run by the agent has the normal permissions of your user account. Use care with prompts and files you do not trust.

## Calculator Example

The included calculator evaluates whitespace-separated arithmetic expressions using `+`, `-`, `*`, and `/`, with standard operator precedence.

Run it directly:

```bash
python calculator/main.py "3 + 5 * 2"
```

## Tests

The test scripts are standalone Python programs. Run them from the project root:

```bash
python test_get_files_info.py
python test_get_file_content.py
python test_run_python_file.py
python test_write_file.py
```